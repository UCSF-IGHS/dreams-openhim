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
        status_code = self.call_dreams_interventions_api(converted_json)
        response = json.dumps({"dreams_api_response": status_code})
        return HttpResponse(response, content_type='application/json')

    def call_dreams_interventions_api(self, data):
        api_conf = copy(settings.DREAMS_INTERVENTION_API_ENDPOINT_CONF)
        headers = {"Content-Type": "application/json"}
        response = requests.post(url=api_conf['api_end_point'], headers=headers,
                                 data=data, auth=HTTPBasicAuth(api_conf['api_user_name'],
                                                               api_conf['api_password']))

        orchestrationsResults = []
        orchestrationsResults = []
        timestamp = datetime.now()
        orchestrationsResults.append({
            name: 'Post DREAMS Intervention',
            request: {
                path: request.path,
                headers: request.headers,
                querystring: request.originalUrl.replace(request.path, ''),
                body: request.body,
                method: request.method,
                timestamp: timestamp
            },
            response: {
                status: response.status_code,
                body: JSON.stringify(response.body, null, 4),
                timestamp: timestamp
            }
        })
        properties = {}
        openhim_response = {
            status: response.status_code,
            headers: {
                'content-type': 'application/json'
            },
            body: JSON.stringify(response.body, null, 4),
            timestamp: timestamp
        }
        returnObject = {
            'x-mediator-urn': {},
            status: response.status_code,
            response: openhim_response,
            orchestrations: orchestrationsResults,
            properties: properties
        }                                                    
        return returnObject
