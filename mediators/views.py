from django.http import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from mediators.dreams_intervention_mediator import DreamsInterventionMediator
from .echo_mediator import EchoMediator


def index(request):
    return HttpResponse("Hello, world. You're at the him-mediators-app index.")


class RegisterEchoAPIView(APIView):
    def get(self, request):
        mediator = EchoMediator()
        mediator.register()
        return Response("Mediator Registered Successfully", status.HTTP_200_OK)


class EchoAPIView(APIView):
    def post(self, request):
        return Response(self.request.data, status.HTTP_200_OK)


class RegisterDreamsInterventionMediatorAPIView(APIView):
    def get(self, request):
        mediator = DreamsInterventionMediator()
        mediator.register()
        return Response("Mediator Registered Successfully", status.HTTP_200_OK)


class DreamsInterventionMediatorAPIView(APIView):
    def post(self, request):
        mediator = DreamsInterventionMediator()
        converted_json = mediator.convert_to_dream_intervention_api_json(self.request.data)
        return HttpResponse(converted_json, content_type='application/json')
