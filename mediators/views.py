from django.http import HttpResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .echo_mediator import EchoMediator


def index(request):
    return HttpResponse("Hello, world. You're at the him-mediators-app index.")


class RegisterEchoAPIView(APIView):
    def post(self, request):
        print('Initialize Mediator')
        EchoMediator()
        return Response("Working", status.HTTP_200_OK)


class EchoAPIView(APIView):
    def post(self, request):
        return Response(self.request.data, status.HTTP_200_OK)


class RegisterDreamsODKAPIView(APIView):
    def post(self, request):
        print('Initialize Mediator')
        EchoMediator()
        return Response("Working", status.HTTP_200_OK)


class DreamsODKAPIView(APIView):
    def post(self, request):
        # get DREAMS APP API
        # change json format
        # response with the json
        return Response(self.request.data, status.HTTP_200_OK)

# ODK -> OpenHIM -> DreamsODKAPIView -> OpenHIM -> DREAMS app