import resilient
from resilient_lib import build_incident_url, build_resilient_url
from datetime import datetime
import pytz

class ResilientRestClient():
    def __init__(self, key, sec, host, port, org, cafile):
        self.resilient_key = key
        self.resilient_secret = sec
        self.resilient_host = host
        self.resilient_port = port
        self.resilient_org = org
        self.cafile = cafile
    
    
    def get_resilient_rest_client(self):
        data = {
            "api_key_id": self.resilient_key,
            "api_key_secret": self.resilient_secret,
            "host": self.resilient_host, 
            "port": self.resilient_port, 
            "org": self.resilient_org,
            "cafile": self.cafile
            }
        return resilient.get_client(data)

    def get_all_incidents(self):
        # Creating Resilient REST Client
        __rest_client = self.get_resilient_rest_client()
        # needs to add additional data filed in the url like below one, have a list in the seetings then
        #populate this url based on those custom fileds
        #/incidents/query_paged?field_handle=incident_level&field_handle=last_update_by_client&return_level=normal
        INCIDENT_QUERY_PAGED = "/incidents/query_paged?field_handle=incident_level&field_handle=last_update_by_client&field_handle=incident_is_work_in_progress_flag&field_handle=attack_Name&return_level=normal&handle_format=names"
        all_incidents = []
        start_inc_num = 0
        ret_num = 0
        query_incident = True
        page_size = 1000
        while query_incident:
            body = {"filters": [
                {"conditions": [{"method": "not_equals", "field_name": "plan_status", "value": ["C"], "evaluation_id": 1}],
                "logic_type": "ALL", "type_handle": {"name": "incident"}}], "start": start_inc_num, "length": page_size,
                    "recordsTotal": page_size}
            ret = __rest_client.post(uri=INCIDENT_QUERY_PAGED, payload=body, timeout=5000)
            data = ret.get("data", [])
            ret_num = len(data)
            if ret_num > 0:
                print("Downloaded {} incidents, total now {} ...".format(ret_num, ret_num + start_inc_num))
                all_incidents.extend(data)
            else:
                # No more incidents to read
                query_incident = False
            start_inc_num += ret_num
        return all_incidents


def download_instance_incident_data(conf_instance: list = [], download_instance: list = []):    
    __instance_inc_data = {}
    for instance in conf_instance:
        if instance.get("host") in download_instance:
            rest_cls_obj = ResilientRestClient(key=instance.get("key"), sec=instance.get("sec"), host=instance.get("host"),
            port=instance.get("port"), org=instance.get("org"), cafile=instance.get("cafile"))
            __inc_data = rest_cls_obj.get_all_incidents()
            __instance_inc_data[rest_cls_obj.resilient_host] = __inc_data
    return __instance_inc_data

def build_incident_open_url(host, port, inc_id, org_id):
    return build_incident_url(build_resilient_url(host, port), inc_id, org_id)

def convert_epoch_utc_date_time(epoch_milli, format_str="%Y-%m-%dT%H:%M:%SZ"):
    if epoch_milli:
        epoch_sec = int(epoch_milli) / 1000
        utc_dt = datetime.utcfromtimestamp(epoch_sec)
        utc_dt = pytz.UTC.localize(utc_dt)
        return datetime.strftime(utc_dt, format_str)
    else:
        return None

