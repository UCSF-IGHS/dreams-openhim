from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class EchoAPIView(APIView):
    def post(self, request):
        return Response(self.request.data, status.HTTP_200_OK)
