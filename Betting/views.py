from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CreateLeague(APIView):
    def post(self, request, format='json'):
        print('posted')
        return Response(status=status.HTTP_200_OK)