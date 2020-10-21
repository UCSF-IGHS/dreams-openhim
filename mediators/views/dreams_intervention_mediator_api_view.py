import json

import requests
from django.http import HttpResponse
from requests.auth import HTTPBasicAuth
from rest_framework.views import APIView
from copy import copy

from django.conf import settings
from mediators.dreams_intervention_mediator import DreamsInterventionMediator
from datetime import datetime


class DreamsInterventionMediatorAPIView(APIView):
    def post(self, request):
        mediator = DreamsInterventionMediator()
        request_body = request.body.decode("utf-8")
        converted_json = mediator.convert_to_dream_intervention_api_json(self.request.data)
        api_response = self.call_dreams_interventions_api(converted_json)
        orchestration_results = self.generate_orchestration_results(request, request_body, api_response)
        response = json.dumps(orchestration_results)
        return HttpResponse(response, content_type='application/json')

    def call_dreams_interventions_api(self, data):
        api_conf = copy(settings.DREAMS_INTERVENTION_API_ENDPOINT_CONF)
        headers = {"Content-Type": "application/json"}
        response = requests.post(url=api_conf['api_end_point'], headers=headers,
                                 data=data, auth=HTTPBasicAuth(api_conf['api_user_name'],
                                                               api_conf['api_password']))
        return response

    def generate_orchestration_results(self, request, request_body, response):
        mediator_conf = copy(settings.DREAMS_INTERVENTION_MEDIATOR_CONF)
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        orchestrations_results = [{
            "name": "Post DREAMS Intervention",
            "request": {
                "path": request.path,
                "headers": request.headers._store,
                "querystring": None,
                "body": json.loads(request.body),
                "method": request.method,
                "timestamp": ""
            },
            "response": {
                "status": response.status_code,
                "body": json.loads(request.body),
                "timestamp": timestamp
            }
        }]

        openhim_response = {
            "status": response.status_code,
            "headers": {
                "content-type": "application/json"
            },
            "body": json.loads(request.body),
            "timestamp": timestamp
        }

        properties = {
            "interventions_count": len(json.loads(request.body))
        }

        return_object = {
            "x-mediator-urn": mediator_conf['urn'],
            "status": response.status_code,
            "response": openhim_response,
            "orchestrations": orchestrations_results,
            "properties": properties
        }
        return return_object
