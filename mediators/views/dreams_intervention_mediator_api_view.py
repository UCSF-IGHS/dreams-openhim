import json

import requests
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from requests.auth import HTTPBasicAuth
from rest_framework.views import APIView
from rest_framework import status as status_codes
from copy import copy

from django.conf import settings
from mediators.dreams_intervention_mediator import DreamsInterventionMediator
from datetime import datetime

from mediators.mixins.response_status_mixin import ResponseStatusMixin


class DreamsInterventionMediatorAPIView(APIView, ResponseStatusMixin):

    def post(self, request):
        mediator = DreamsInterventionMediator()
        interventions = mediator.extract_interventions(self.request.data)

        orchestration_results = []
        for intervention in interventions:
            api_response = self.upload_intervention_to_dreams_api(intervention)
            orchestration_result = self.generate_orchestration_result(api_response, intervention)
            orchestration_results.append(orchestration_result)

        mediator_response = self.generate_mediator_response(request, orchestration_results)
        response = json.dumps(mediator_response)
        return HttpResponse(response, content_type='application/json')

    def upload_intervention_to_dreams_api(self, intervention):
        if isinstance(intervention, list):
            raise ValidationError('Found multiple interventions. Only one intervention can be uploaded per call')

        api_conf = copy(settings.DREAMS_INTERVENTION_API_ENDPOINT_CONF)
        headers = {"Content-Type": "application/json"}
        response = requests.post(url=api_conf['api_end_point'], headers=headers, data=json.dumps(intervention),
                                 auth=HTTPBasicAuth(api_conf['api_user_name'], api_conf['api_password']))
        return response

    def generate_mediator_response(self, request, orchestration_results):
        mediator_conf = copy(settings.DREAMS_INTERVENTION_MEDIATOR_CONF)
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        status = ResponseStatusMixin.MEDIATOR_RESPONSE_SUCCESSFUL

        try:
            for orchestration_result in orchestration_results:
                response_status = orchestration_result['response']['body']['status']
                if response_status != ResponseStatusMixin.SUCCESS_CREATED and response_status != ResponseStatusMixin.SUCCESS_DUPLICATE_IGNORED:
                    status = ResponseStatusMixin.MEDIATOR_RESPONSE_COMPLETED
                    break
        except:
            status = ResponseStatusMixin.MEDIATOR_RESPONSE_FAILED

        response_to_originating_client = {
            "status": status_codes.HTTP_200_OK,
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
            "orchestrations": orchestration_results,
            "properties": {
                "interventions_count": len(orchestration_results)
            }
        }
        return return_object

    def generate_orchestration_result(self, response, intervention):
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        orchestrations_result = {
            "name": "Post DREAMS Intervention",
            "request": {
                "path": response.request.path_url,
                "headers": dict(response.request.headers),
                "querystring": None,
                "body": intervention,
                "method": response.request.method,
                "timestamp": timestamp
            },
            "response": {
                "status": response.status_code,
                "body": json.loads(response.content),
                "timestamp": timestamp
            }
        }
        return orchestrations_result
