from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from mediators.echo_mediator import EchoMediator


class RegisterEchoAPIView(APIView):
    def get(self, request):
        mediator = EchoMediator()
        mediator.register()
        return Response("Mediator Registered Successfully", status.HTTP_200_OK)
