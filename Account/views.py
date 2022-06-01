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

            userObj = User.objects.create_user(email=email, password=password)
            userObj.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CurrentUser(APIView):
    def get(self, request, format='json'):
        json = {}
        if request.user.is_authenticated:
            # print(request.user)
            json['email'] = request.user.email
            json['isLoggedIn'] = True

            return Response(json, status=status.HTTP_200_OK)
        
        json['email'] = ''
        json['isLoggedIn'] = False
        return Response(json, status=status.HTTP_204_NO_CONTENT)
       

class LogIn(APIView):
    serializer_class = LogInSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def post(self, request, format='json'):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')        

            user = authenticate(email=email, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    json = {
                        'email' : user.email,
                        'isLoggedIn' : True
                    }

                    return Response(json, status=status.HTTP_202_ACCEPTED)
                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class Logout(APIView):
    def post(self, request, format=None):
        print(request)
        logout(request)
        return Response(status=status.HTTP_200_OK)

