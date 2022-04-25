from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

# Create your views here.
class CreateLeague(APIView):
    serializer_class = CreateLeagueSerializer

    def post(self, request, format='json'):
        league = self.serializer_class(data=request.data)

        if league.is_valid():
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST) 