import json

import requests
from django.http import HttpResponse
from requests.auth import HTTPBasicAuth
from rest_framework.views import APIView
from copy import copy

from django.conf import settings
from mediators.dreams_intervention_mediator import DreamsInterventionMediator
from datetime import datetime

from django.contrib.sites.shortcuts import get_current_site

class DreamsInterventionMediatorAPIView(APIView):
    def post(self, request):
        mediator = DreamsInterventionMediator()
        request_body = request.body.decode("utf-8")
        converted_json = mediator.convert_to_dream_intervention_api_json(self.request.data)
        status_code = self.call_dreams_interventions_api(converted_json, request, request_body)
        response = json.dumps({"dreams_api_response": status_code})
        return HttpResponse(response, content_type='application/json')

    def call_dreams_interventions_api(self, data, request):
        api_conf = copy(settings.DREAMS_INTERVENTION_API_ENDPOINT_CONF)
        headers = {"Content-Type": "application/json"}
        response = requests.post(url=api_conf['api_end_point'], headers=headers,
                                 data=data, auth=HTTPBasicAuth(api_conf['api_user_name'],
                                                               api_conf['api_password']))

        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        orignal_url = get_current_site(request).domain

        orchestrations_results = []
        orchestrations_results.append(json.dumps({
            "name": "Post DREAMS Intervention",
            "request": {
                "path": request.path,
                #"headers": json.dumps(request.headers),
                "querystring": orignal_url,
                "body": request_body,
                "method": request.method,
                "timestamp": ""
            },
            "response": {
                "status": response.status_code,
                "body": request_body,
                "timestamp": ""
            }
        }))
        properties = {}
        openhim_response = {
            "status": response.status_code,
            "headers": {
                "content-type": "application/json"
            },
            "body": request_body,
            "timestamp": timestamp
        }
        return_object = {
            "x-mediator-urn": {},
            "status": response.status_code,
            "response": openhim_response,
            "orchestrations": orchestrations_results,
            "properties": properties
        }                                                    
        return json.dumps(return_object)
