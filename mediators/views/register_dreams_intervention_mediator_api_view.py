from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from mediators.dreams_intervention_mediator import DreamsInterventionMediator


class RegisterDreamsInterventionMediatorAPIView(APIView):
    def get(self, request):
        mediator = DreamsInterventionMediator()
        mediator.register()
        return Response("Mediator Registered Successfully", status.HTTP_200_OK)
