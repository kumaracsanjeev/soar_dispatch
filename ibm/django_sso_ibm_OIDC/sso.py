# Author: IBM penguins Squad, Guadalajara MX
# july 2019

# this class is to support IBM SSO
# written using the authentication layer openID Connect 1.0
# openID Connect 1.0 standard is not controlled by IBM, is
# controlled by the OpenID Foundation.

# python dependencies
from requests.utils import requote_uri
import requests
import json

# third party dependencies
from django.conf import settings
import jwt
from django.shortcuts import redirect

class Sso:

    def __init__(self,authorize_url,token_url,client_id,client_secret,redirect_url):
        """

        :param authorize_url:   authorize url provided by SSO Self Service
        :param token_url:       token url provided by SSO Self Service
        :param client_id:       client id url provided by SSO Self Service
        :param client_secret:   client secret provided by SSO Self Service
        :param redirect_url:    redirect url that it was set in SSO self service, in the self service page you can set
                                more than one redirect url, the url redirect is the url where the user will be redirect
                                only when he pass the ibm authorization, if you tried to redirect to another URL in
                                your site and that site it was not registered in the SSO self service you will get an
                                error.
        """
        self.authorize_url = authorize_url
        self.token_url = token_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_url = redirect_url

    def generateAuthorizationUrl(self,request):
        """

        :param request: Django HttpRequest object, this object has all request information, you can catch HttpRequest
                        object in the view
        :return:        str that contains the URL where you have to redirect the browser in order to start the sso flow
        """
        protocol = "https://" if request.is_secure() else "http://"
        state = protocol + request.META["HTTP_HOST"] + request.path
        return requote_uri(self.authorize_url + "?scope=openid&response_type=code&client_id=" + self.client_id + "&redirect_uri=" + self.redirect_url)

def ibmSsoCallBack(function):
    """
    IMPORT NOTE: This decorator should be applied in all request functions (in your views file) that you want to
    protect by IBM SSO. Appying this decorator, the request will be process only if the user has been allowed by
    IBM. You must at least apply this decorator in the function that process the redirect URI tha comes from IBM
    you have to remember that this value was set it in the IBM SSO self service, otherwise the validation data that
    come from IBM will not be stored in the web session and even if you apply the decorator in other request
    function and the user has been logged in IBM this decorator will think that the user has been not logged yet

    this decorator it must be applied to a request function in the views.py, when the decorator it's applied one of the
    following scenarios will occur

    - the decorator detect that exists the "code" parameter that has been passed by GET https method, that means that
      the request came from IBM SOO authorization endpoint (code parameter is added by IBM), now the decorator will
      try to generated an access token. This code only can be used one time, if you try to generated more than one
      access token using this code you will get an error, this is design to avoid that someone inject a fake or old code
      in the URL with the purpose of generated an access token. With the code, the decorator will try to generated
      an access token, to do this the decorator will send the code to the token endpoint. If the response from the
      token endpoint it's an error means that the access token was no generated, due that the code is not valid, the
      decorator will redirect the browser to authorization endpoint to start again the SSO authorization flow. If the
      response to the token endpoint is successful, the endpoint will response with json that contains some relevant
      information as can be access_token, refresh_token, full user name, email address. This information will be stored
      in the Django session as python dict in the variable "ssoTokenContents". Finally due that the decorator is able to
      get a valid content from token endpoint means that the user has logged correctly in IBM , now the source code from
      the request where this decorator is applied it's going to be executed (views.py file). In the request
      (views.py file) you can retrieve the content using something like this

        request.session["ssoTokenContents"]["sso_access_token"]

      where ssoTokenContents is the python dict that contains whole the information that came from the token, and
      sso_access_token is the key to get the access_token. In the next json you can see an example of data that is
      stored in the ssoTokenContents (stored in the session)

        {
          "sso_access_token": "AAAAAAAAABBBBBBBBBBBBBBBBCCCCCCCCCCCCDDD",
          "sso_refresh_token": "AAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBCCCCCCDDCDD"
          "iss": "https://dpev069a.innovate.ibm.com/isam",
          "at_hash": "LGbwy1Cf2MYWrXT15OvAbQ",
          "sub": "someone@us.ibm.com",
          "lastName": "Smith",
          "realmName": "https://dpev069a.innovate.ibm.com",

          "uid": "074834897",
          "dn": "uid=074834897,c=us,ou=bluepages,o=ibm.com",
          "userAgent": "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0",
          "cn": "Peter D. Birk",
          "aud": "L5AGefM1Als8bhBDPW6W",
          "firstName": "Peter",
          "emailAddress": "someone@us.ibm.com",
          "blueGroups": [
             "blueid-adopters-techcontacts",
            "SSOSelfBoardingReports",
            "SSOSelfBoardingReportsProduction",
            "MSO365MAC",
            "OTP_Service-DevTest",
            "SSOSelfBoardingW3IDMonitor",
            "SSOSelfBoardingW3LegacyMonitor",
            "SSOSelfBoardingInnovationMonitor",
            "w3ID_IDService_API",
            "OTP_Service-Pilot"
          ],
          "clientIP": "x.x.x.x",
          "exp": 1458019395,
          "authMethod": "password",
          "iat": 1458012195
        }

    - the decorator detect that the web session has expired or web the session it doesn't exist, in this case the
        decorator will redirect the browser to the authorization endpoint, in order to login the user with his
        w3 credentials, the sso flow it will start. when this occur the request function where this decorator is
        applied it won't be executed due that the application doesn't found a alive session. You have to remember
        that if the authorization is passed the SSO IBM will redirect to the redirect URL that you have set

    - the decorator detect that exists a alive and valid web session(valid when the session has ssoTokenContents dict),
        now the decorator will try to refresh the w3 session in order to know if the user still logged in in IBM, to do
        this the decorator will make a request to the token endpoint (with POST method), in the request to the token
        endpoint the decorator will attach the refresh_token that it has been stored in the session. If the response
        from the token endpoint is an error,  the decorator will redirect the browser to the authorization endpoint,
        in order to login again the user with his w3 credentials, the sso flow it will start. If the response to
        the token endpoint is successful the response will contains a new access_token and a new refresh_token that
        will be saved in the web session (overwriting the old values of this variables). Finally due that the decorator
        is able to refresh the access_token means that the user still logged correctly in IBM , now the source code from
        the request where this decorator is applied it's going to be executed (views.py file).

        IMPORTANT NOTE REGARDING TOKEN CONTENT
        IBM sso guide say this " There's no /userinfo endpoint in ISAM OIDC yet" the unique relevant information that
        it's able to get are: name, email. And also to reload this data is necessary make a new request to
        authorization endpoint, in this scenario the only thing that is do it is refresh the token in order to know if
        the user still logged in in IBM

    - if none of these scenarios are met the decorator will redirect the browser to the authorization endpoint to start
      again the authorization flow


    :param function: Django web request function (that it's stored in view)
    :return:
    """
    def functionToRun(*args, **kwargs):
        requestData = args[0]
        ibm_sso = Sso(
            authorize_url=settings.SSO_AUTHORIZE_URL,
            token_url=settings.SSO_TOKEN_URL,
            client_id=settings.SSO_CLIENT_ID,
            client_secret=settings.SSO_CLIENT_SECRET,
            redirect_url=settings.SSO_REDIRECT_URL)
        if "code" in requestData.GET:
            # request came from authorization endpoint the flow has just started
            authorizationCode = requestData.GET["code"]
            requestHeaders = {"Content-type": "application/x-www-form-urlencoded"}
            host_name = requote_uri(ibm_sso.token_url)
            data = "code=" + authorizationCode + "&grant_type=authorization_code&client_id=" \
                   + ibm_sso.client_id + "&client_secret=" + ibm_sso.client_secret + "&redirect_uri=" \
                   + ibm_sso.redirect_url
            responseAsDict = json.loads(requests.post(host_name, data=data, headers=requestHeaders).text)
            if "error_description" in responseAsDict:
                # the user tried to use an old code for authorization, the user will be redirect
                # to authorization endpoint to start again the flow
                return redirect(ibm_sso.generateAuthorizationUrl(request=requestData))

            jwt_options = {
                'verify_signature': False,
                'verify_exp': False,
                'verify_nbf': False,
                'verify_iat': False,
                'verify_aud': False
            }
            requestData.session["ssoTokenContents"] = jwt.decode(
                str(responseAsDict["id_token"]),
                responseAsDict["access_token"],
                algorithms=['HS256'],
                options=jwt_options)
            requestData.session["ssoTokenContents"]["sso_access_token"] = responseAsDict["access_token"]
            requestData.session["ssoTokenContents"]["sso_refresh_token"] = responseAsDict["refresh_token"]
            requestData.session.modified = True

        elif "ssoTokenContents" not in requestData.session:
            # access denied due that web session it doesn't exist, the web session has expired,
            # the browser it will be redirected to authorization endpoint to start again the sso flow
            return redirect(ibm_sso.generateAuthorizationUrl(request=requestData))
        elif "ssoTokenContents" in requestData.session and "sso_refresh_token" in requestData.session["ssoTokenContents"]:
            # refresh token in order to validate if the credentials still valid, the validation is done by IBM
            # IBM sso guide say this " There's no /userinfo endpoint in ISAM OIDC yet" the unique relevant
            # information that it's able to get are: name, email. And also to reload this data is necessary make
            # a new request to authorization endpoint, here the only thing that is do it is refresh the token
            host_name = requote_uri(ibm_sso.token_url)
            requestHeaders = {"Content-type": "application/x-www-form-urlencoded"}
            data = "refresh_token=" + requestData.session["ssoTokenContents"]["sso_refresh_token"] \
                   + "&grant_type=refresh_token&client_id=" + ibm_sso.client_id \
                   + "&client_secret=" + ibm_sso.client_secret
            responseAsDict = json.loads(requests.post(host_name, data=data, headers=requestHeaders).text)

            if "error_description" in responseAsDict:
                # error refreshing token, maybe it's not valid. The user will be redirect
                # to authorization endpoint to start again the flow
                return redirect(ibm_sso.generateAuthorizationUrl(request=requestData))

            requestData.session["ssoTokenContents"]["sso_access_token"] = responseAsDict["access_token"]
            requestData.session["ssoTokenContents"]["sso_refresh_token"] = responseAsDict["refresh_token"]
            requestData.session.modified = True
        else:
            # access denied due token is not valid, or token wasn't able to be refreshed, the browser it will
            # be redirected to authorization endpoint to start again the sso flow.
            # If the token is not valid or wasn't able to be reloaded maybe the ibm use
            # has changed his password or credentials provided are not valid
            return redirect(ibm_sso.generateAuthorizationUrl(request=requestData))

        #  if the code came to this point the token is valid and that means that
        #  the user is logged in and the original request can be process

        return function(*args, **kwargs)
    return functionToRun
