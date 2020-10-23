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
        converted_json = mediator.convert_to_dream_intervention_api_json(self.request.data)
        api_response = self.call_dreams_interventions_api(converted_json)
        orchestration_results = self.generate_orchestration_results(request, api_response)
        response = json.dumps(orchestration_results)
        return HttpResponse(response, content_type='application/json', status=api_response.status_code)

    def call_dreams_interventions_api(self, data):
        api_conf = copy(settings.DREAMS_INTERVENTION_API_ENDPOINT_CONF)
        headers = {"Content-Type": "application/json"}
        response = requests.post(url=api_conf['api_end_point'], headers=headers, data=data,
                                 auth=HTTPBasicAuth(api_conf['api_user_name'], api_conf['api_password']))
        return response

    def generate_orchestration_results(self, request, response):
        mediator_conf = copy(settings.DREAMS_INTERVENTION_MEDIATOR_CONF)
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        orchestrations_results = [{
            "name": "Post DREAMS Intervention",
            "request": {
                "path": response.request.path_url,
                "headers": dict(response.request.headers),
                "querystring": None,
                "body": json.loads(response.request.body),
                "method": response.request.method,
                "timestamp": timestamp
            },
            "response": {
                "status": response.status_code,
                "body": json.loads(response.content),
                "timestamp": timestamp
            }
        }]

        properties = {
            "interventions_count": len(json.loads(response.request.body))
        }

        response_status = {
            "processing": 'Processing',
            "failed": 'Failed',
            "completed": 'Completed',
            "successful": 'Successful',
            "with_errors": 'Completed with error(s)'
        }
        status = ''
        if 100 <= response.status_code <= 199:
            status = response_status['processing']
        elif 200 <= response.status_code <= 299:
            status = response_status['successful']
        elif 300 <= response.status_code <= 399:
            status = response_status['completed']
        elif 400 <= response.status_code <= 499:
            status = response_status['completed']
        elif 500 <= response.status_code <= 599:
            status = response_status['failed']

        response_to_originating_client = {
            "status": 200,
            "headers": {
                "content-type": "application/json"
            },
            "body": request.data,
            "timestamp": timestamp
        }

        return_object = {
            "x-mediator-urn": mediator_conf['urn'],
            "status": status,
            "response": response_to_originating_client,
            "orchestrations": orchestrations_results,
            "properties": properties
        }
        return return_object
