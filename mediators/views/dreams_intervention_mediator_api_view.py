from django.http import HttpResponse
from rest_framework.views import APIView

from mediators.dreams_intervention_mediator import DreamsInterventionMediator


class DreamsInterventionMediatorAPIView(APIView):
    def post(self, request):
        mediator = DreamsInterventionMediator()
        converted_json = mediator.convert_to_dream_intervention_api_json(self.request.data)
        return HttpResponse(converted_json, content_type='application/json')
