from django.urls import path
from . import views
from ibm.django_sso_ibm_OIDC import views as sso_views

urlpatterns = [
    path("", views.redirect_login),
    path("login", views.Login.as_view(), name="login_url"),
    path("account/login", views.LoginView, name="sso_login_url"),
    path("ibm_sso_login", sso_views.request_authorization_endpoint, name="ibm_ssologin"),
    path("soar/incident/dispatch/inc_inst", views.soar_incidents_by_instance.as_view(), name="inc_inst"),
    path("soar/incident/dispatch/all_inc", views.soar_all_incidents, name="all_inc"),
    path("soar/incident/dispatch/all_asgn_inc", views.soar_assigned_incidents, name="all_asgn_inc"),
    path("soar/incident/dispatch/dashboard/analytic", views.soar_incident_analytics, name="soar_analytic_dashboard"),
    path("update", views.update_incident_asignee),
    path("logout", views.user_logout, name="logout")
    ]
