from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

# Create your views here.
class CreateUser(APIView):
    serializer_class = CreateUserSerializer

    def post(self, request, format='json'):
        user = self.serializer_class(data=request.data)

        if user.is_valid():
            email = user.data.get('email')
            password = user.data.get('password')

            userObj = User.objects.create_user(email=email, password=password)
            userObj.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)