from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')

class LogInSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        email = data.get('email')

        try:
            user_obj = get_object_or_404(User, email=email)
        except:
            raise serializers.ValidationError("Email Does Not Exist")
        
        password = data.get('password')

        if not password:
            raise serializers.ValidationError("Please Enter a password")
        
        if user_obj:
            data['user'] = user_obj

        return data