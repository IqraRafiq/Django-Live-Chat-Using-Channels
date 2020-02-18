from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings


from accounts import models
from accounts import serializers
from accounts import permissions
# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

#  login
class UserLoginApiView(ObtainAuthToken):
    """handle creating user authentication login"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES