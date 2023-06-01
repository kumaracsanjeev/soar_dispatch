from collections import Counter
from itertools import count
import json
from resilient_lib import clean_html
from audioop import reverse
from django.shortcuts import redirect, render
from django.views import View
from django.urls import reverse
from ibm.django_sso_ibm_OIDC.sso import ibmSsoCallBack
from django.http import HttpResponseBadRequest, HttpResponse
from django.contrib.auth import logout
from django.core.cache import cache
from django.conf import settings
from django.db.models import Q
from .resilient_rest_client import download_instance_incident_data, build_incident_open_url, convert_epoch_utc_date_time

from .models import ResilientIncidentsData
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

ST_MAP = {"A": "Active", "D": "Deactivated", "I": "Inactive", "P": "Pending activation", "R": "Password Reset Pending",
          "U": "unknown"}

def redirect_login(request):
    return redirect(reverse("login_url"))

class Login(View):
    def get(self, request):
        return render(request, "soar_incident_dispatcher_app/login.html")
    def post(self, request):
        return redirect(reverse("sso_login_url"))

@ibmSsoCallBack
def LoginView(request):
    if request.method == "GET":
        return redirect(reverse("soar_analytic_dashboard"))
    else: 
        return HttpResponseBadRequest("Method Not allowed")

@ibmSsoCallBack
def soar_incident_analytics(request):
    if request.method == "GET":
        name = request.session["ssoTokenContents"]["name"]
        first_name = request.session["ssoTokenContents"]["firstName"]
        email = request.session["ssoTokenContents"]["emailAddress"]

        # Reading the Resilient Instance configuration from settings file
        res_conf = settings.RES_CONFIG
        all_instance = {} # Dict to store instance as key & Org as Value
        down_instance = [] # list of instance which is not available in DB & to be downloaded
        for each_obj in res_conf:
            if each_obj.get("host") not in all_instance:
                all_instance[each_obj.get("host")] = each_obj.get("org")
                
                # Checking DB for instance data, if not available add to download list 
                av_db_host = ResilientIncidentsData.objects.filter(resilient_host=each_obj.get("host"))
                if not av_db_host:
                    down_instance.append(each_obj.get("host"))

        # Getting all instance Incident Data
        incident_data = download_instance_incident_data(conf_instance=res_conf, download_instance=down_instance)
        with open("inc.json", "w+") as fh:
            json.dump(incident_data, fh)
        # Save the new instance incident Data to DB
        for __ins_host, __data in incident_data.items():
            for each_obj in res_conf:
                if __ins_host == each_obj.get("host"):
                    __port = each_obj.get("port")
            for __inc_data in __data:
                cust_field_data = __inc_data.get("properties")
                incident_level = cust_field_data.get("incident_level")
                if incident_level not in ["Triage Only", "Investigation Complete"]:
                    db_object = ResilientIncidentsData(resilient_host=__ins_host, incident_id=__inc_data.get("id"),
                        incident_name=__inc_data.get("name"), siem_rule_name=clean_html(cust_field_data.get("attack_Name")),
                        date_created=__inc_data.get("create_date"),last_update_by_client = cust_field_data.get("last_update_by_client"),
                        incident_is_work_in_progress_flag = cust_field_data.get("incident_is_work_in_progress_flag"),
                        incident_level = cust_field_data.get("incident_level"),incident_handler_triag=__inc_data.get("owner_id"), 
                        phase=__inc_data.get("phase_id"),severity=__inc_data.get("severity_code"), 
                        org=__inc_data.get("org_handle"), status=ST_MAP.get(__inc_data.get("plan_status")), 
                        open_url = build_incident_open_url(__ins_host, __port, __inc_data.get("id"), __inc_data.get("org_id")))
                    db_object.save()

        # Getting all the incidents from DB
        all_inst = []  # List store all available instace IP/DNS
        all_severity = [] # list store incident all available severity
        all_phase = [] # List to store all available phase
        db_inc_data = ResilientIncidentsData.objects.all().order_by("incident_id")
        for each_obj in db_inc_data:
            all_inst.append(each_obj.resilient_host)
            all_severity.append(each_obj.severity)
            all_phase.append(each_obj.phase)
        inc_cnt_by_inst = dict(Counter(all_inst))
        inc_cnt_by_sev = dict(Counter(all_severity))
        inc_cnt_by_phase = dict(Counter(all_phase))
        return render(request, "soar_incident_dispatcher_app/incidents_analytics.html",
         context={'user_first_letter': first_name[0], 'user': name, 'email': email, "inc_cnt_by_inst": inc_cnt_by_inst,
         "inc_cnt_by_sev": inc_cnt_by_sev, "inc_cnt_by_phase": inc_cnt_by_phase})
    else:
        return HttpResponseBadRequest("Method Not allowed.")

class soar_incidents_by_instance(View):
    def get(self, request):
        if "ssoTokenContents" not in dict(request.session):
            return redirect(reverse("sso_login_url"))
        name = request.session["ssoTokenContents"]["name"]
        first_name = request.session["ssoTokenContents"]["firstName"]
        email = request.session["ssoTokenContents"]["emailAddress"]
        res_conf = settings.RES_CONFIG
        all_instance = {}
        down_instance = []
        for each_obj in res_conf:
            if each_obj.get("host") not in all_instance:
                all_instance[each_obj.get("host")] = each_obj.get("org")

        # Getting all the Data from DB
        processed_data = dict()
        db_inc_data = ResilientIncidentsData.objects.all().order_by("incident_id")
        for each_obj in db_inc_data:
            if each_obj.resilient_host not in processed_data:
                processed_data[each_obj.resilient_host] = []
            if each_obj.asignee_email == "" or each_obj.asignee_email is None:
                processed_data[each_obj.resilient_host].append({"id": each_obj.incident_id, "name": each_obj.incident_name, 
                "siem_rule_name": each_obj.siem_rule_name, "dt_crt": convert_epoch_utc_date_time(each_obj.date_created),
                "last_update_by_client": each_obj.last_update_by_client,"incident_is_work_in_progress_flag": each_obj.incident_is_work_in_progress_flag,
                "incident_level": each_obj.incident_level,"triag": each_obj.incident_handler_triag,"phase": each_obj.phase,"severity": each_obj.severity,
                "org": each_obj.org,"st": each_obj.status,"url": each_obj.open_url,"assignee": each_obj.asignee_email})
        return render(request, "soar_incident_dispatcher_app/incidents_by_instance.html", 
        context={'user_first_letter': first_name[0], 'user': name, 'email': email, "all_instance": all_instance, "inc_data": processed_data})
    
    def post(self, request):
        if "ssoTokenContents" not in dict(request.session):
            return redirect(reverse("sso_login_url"))
        name = request.session["ssoTokenContents"]["name"]
        first_name = request.session["ssoTokenContents"]["firstName"]
        email = request.session["ssoTokenContents"]["emailAddress"]
        return render(request, "soar_incident_dispatcher_app/incidents_by_instance.html", 
        context={'user_first_letter': first_name[0], 'user': name, 'email': email})

@ibmSsoCallBack
def soar_all_incidents(request):
    if request.method == "GET":
        name = request.session["ssoTokenContents"]["name"]
        first_name = request.session["ssoTokenContents"]["firstName"]
        email = request.session["ssoTokenContents"]["emailAddress"]
        
        # Getting all the Data from DB
        processed_data = dict()
        db_inc_data = ResilientIncidentsData.objects.all().order_by("incident_id")
        for each_obj in db_inc_data:
            if each_obj.resilient_host not in processed_data:
                processed_data[each_obj.resilient_host] = []
            if each_obj.asignee_email == "" or each_obj.asignee_email is None:
                processed_data[each_obj.resilient_host].append({"id": each_obj.incident_id, "name": each_obj.incident_name, 
                "siem_rule_name": each_obj.siem_rule_name, "dt_crt": convert_epoch_utc_date_time(each_obj.date_created),
                "last_update_by_client": each_obj.last_update_by_client,"incident_is_work_in_progress_flag": each_obj.incident_is_work_in_progress_flag,
                "incident_level": each_obj.incident_level,"triag": each_obj.incident_handler_triag,"phase": each_obj.phase,"severity": each_obj.severity,"org": each_obj.org,
                "st": each_obj.status,"url": each_obj.open_url,"assignee": each_obj.asignee_email})
        return render(request, "soar_incident_dispatcher_app/all_incidents.html", 
        context={'user_first_letter': first_name[0], 'user': name, 'email': email, "inc_data": processed_data})
    else:
        return HttpResponseBadRequest("Method not allowed.")

def user_logout(request):
    logout(request)
    cache.clear()
    return redirect("login_url")

@api_view(['POST'])
def update_incident_asignee(request):
    received_data = json.loads(request.body)
    __host, __inc_id = received_data.get("inc_id").split("/")
    print(__host, __inc_id)
    if received_data.get("checked"):
        ResilientIncidentsData.objects.filter(Q(incident_id=__inc_id) & Q(resilient_host=__host)).update(asignee_email=received_data.get("user"))
    else:
        ResilientIncidentsData.objects.filter(Q(incident_id=__inc_id) & Q(resilient_host=__host)).update(asignee_email="")
    return Response({"status": "ok"})

@ibmSsoCallBack
def soar_assigned_incidents(request):
    if request.method == "GET":
        name = request.session["ssoTokenContents"]["name"]
        first_name = request.session["ssoTokenContents"]["firstName"]
        email = request.session["ssoTokenContents"]["emailAddress"]
        
        # Getting all the Data from DB
        processed_data = dict()
        db_inc_data = ResilientIncidentsData.objects.all().order_by("incident_id")
        for each_obj in db_inc_data:
            if each_obj.resilient_host not in processed_data:
                processed_data[each_obj.resilient_host] = []
            if each_obj.asignee_email != "" and each_obj.asignee_email is not None:
                processed_data[each_obj.resilient_host].append({"id": each_obj.incident_id, "name": each_obj.incident_name, 
                "siem_rule_name": each_obj.siem_rule_name, "dt_crt": convert_epoch_utc_date_time(each_obj.date_created),
                "last_update_by_client": each_obj.last_update_by_client,"incident_is_work_in_progress_flag": each_obj.incident_is_work_in_progress_flag,
                "incident_level": each_obj.incident_level,"triag": each_obj.incident_handler_triag,"phase": each_obj.phase,"severity": each_obj.severity,"org": each_obj.org,
                "st": each_obj.status,"url": each_obj.open_url,"assignee": each_obj.asignee_email})
        return render(request, "soar_incident_dispatcher_app/all_incidents.html", 
        context={'user_first_letter': first_name[0], 'user': name, 'email': email, "inc_data": processed_data})
    else:
        return HttpResponseBadRequest("Method not allowed.")
