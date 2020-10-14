from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .echo_mediator import EchoMediator


def index(request):
    return HttpResponse("Hello, world. You're at the him-mediators-app index.")

class EchoAPIView(APIView):
    def post(self, request):
        print('Initialize Mediator')
        echo_mediator = EchoMediator()
        print('Mediator Initialized successfully')
        print(echo_mediator)
        return Response("Working", status.HTTP_200_OK)

# ODK (push) -> OpenHIM -> Mediator -> OpenHIM -> DREAMS