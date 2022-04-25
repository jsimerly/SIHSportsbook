from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError("User must have an email address")

        user = self.model(
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save()
        return user

    def create_super_user(self, email, password):
        if not email:
            raise ValueError("User must have an email address")

        user = self.model(
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.is_admin = True
        user.save()
        return user

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    
    email=models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True
    )

    password=models.CharField(
        max_length=255, 
        null=False
    )

    is_active = models.BooleanField(default=True)

    USERNAME_FIELDS = 'email'
    
    def __str__(self):
        return self.email



