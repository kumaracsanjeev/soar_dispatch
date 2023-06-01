# python dependencies

# third party dependencies
from django.shortcuts import redirect
from django.conf import settings


# module dependencies
from ibm.django_sso_ibm_OIDC.sso import Sso


def request_authorization_endpoint(request):
    ibm_sso = Sso(
        authorize_url=settings.SSO_AUTHORIZE_URL,
        token_url=settings.SSO_TOKEN_URL,
        client_id=settings.SSO_CLIENT_ID,
        client_secret=settings.SSO_CLIENT_SECRET,
        redirect_url=settings.SSO_REDIRECT_URL)
    return redirect(ibm_sso.generateAuthorizationUrl(request=request))
