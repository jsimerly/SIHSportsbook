from rest_framework.views import APIView
from rest_framework.authentication import  SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode   
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

from .utils import generate_token

#Functions
def send_ver_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Activate Your Account'
    email_body = render_to_string(
        'activation.html', 
        {
            'user' : user,
            'domain' : current_site,
            'uid' : urlsafe_base64_encode(force_bytes(user.id)),
            'token' : generate_token.make_token(user)
        }
    )

    email = EmailMessage(
        subject=email_subject,
        body=email_body,
        from_email=settings.EMAIL_FROM_USER,
        to=[user.email],
    )
    email.send()

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

            send_ver_email(userObj, request)

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
        return Response(json, status=status.HTTP_200_OK)
       

class LogIn(APIView):
    serializer_class = LogInSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def post(self, request, format='json'):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')        

            user = authenticate(email=email, password=password)

            if not user.is_email_verified:
                # Get user to verify email
                return Response('Email is not verified, please check your email')

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
        json={}
        json['email'] = ''
        json['isLoggedIn'] = False
        logout(request)
        return Response(json, status=status.HTTP_200_OK)

class Activate_User(APIView):
    def post(self, request, uidb64, token):
        try:
            uid=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)

        except Exception as e: 
            user=None

        if user and generate_token.check_token(user, token):
            user.is_email_verified=True
            user.save()

            return Response('user successfully verified', status=status.HTTP_200_OK)

        return Response('error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
