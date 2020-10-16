from django.http import HttpResponse
from rest_framework.views import APIView


class IndexView(APIView):
    @staticmethod
    def index():
        return HttpResponse("You're at the him-mediators-app index.")
