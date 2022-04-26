from rest_framework.views import APIView
from rest_framework.authentication import  SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from .serializers import *

# Create your views here.
class CreateUser(APIView):
    serializer_class = CreateUserSerializer

    def post(self, request, format='json'):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')

            print('view password: ' + str(password))
            userObj = User.objects.create_user(email=email, password=password)
            userObj.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogIn(APIView):
    serializer_class = LogInSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def post(self, request, format='json'):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')

            tObj = User.objects.get(email=email)
            hashed_pwd = make_password("123456")
            print(hashed_pwd)
            print(tObj.password)

            print(tObj.check_password(password))
            

            user = authenticate(email=email, password=password)
            print(user)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    json = {
                        'email' : user.email
                    }

                    return Response(json, status=status.HTTP_202_ACCEPTED)
                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class Logout(APIView):
    def post(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

