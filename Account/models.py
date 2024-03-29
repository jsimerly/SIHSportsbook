from pyexpat import model
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser

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

    def create_super_user(self, email, password=None):
        if not email:
            raise ValueError("User must have an email address")

        user = self.model(
            email = self.normalize_email(email),
        )

        user.is_admin = True
        user.save()
        return user

class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    
    email=models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True
    )

    password=models.CharField(
        max_length=124, 
        verbose_name='password'
    )

    account_balance = models.DecimalField(
        max_digits=12, 
        decimal_places=2,
        default=0.0
    )

    username = None
    first_name = None
    last_name = None

    is_email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    
    def __str__(self):
        return self.email

