from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user=self.create_user(email,username,password)
        
        user.is_superuser=True
        user.is_staff=True 
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField( max_length=254)
    username=models.CharField(max_length=255, unique=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    
    objects=UserProfileManager()
    
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email']

    def get_full_name(self):
        return self.username 
    
    def get_short_name(self):
        return self.username
# Create your models here.
