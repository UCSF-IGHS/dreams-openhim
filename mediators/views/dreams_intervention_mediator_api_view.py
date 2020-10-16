import json

import requests
from django.http import HttpResponse
from requests.auth import HTTPBasicAuth
from rest_framework.views import APIView
from copy import copy

from django.conf import settings
from mediators.dreams_intervention_mediator import DreamsInterventionMediator


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
        return response.status_code
