from django.shortcuts import render
from django.http import Http404, HttpResponseForbidden
from rest_framework.response import Response
from django.urls import reverse
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


from .models import Thread, ChatMessage
from accounts.models import User
from django.forms.models import model_to_dict
from chating import serializers
from rest_framework.views import APIView

from django.views.generic import DetailView, ListView

class InboxView(ListView):

    def get_queryset(self):
        return Thread.objects.by_user(self.request.user)

class ThreadView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self,request, username):
        user = User.objects.get(name=username)
        thread =  Thread.objects.by_user(self.request.user)

        messages=ChatMessage.objects.filter(thread__second=self.request.user, thread__first=user) 
        # serializer = serializers.MessageSerializer(messages, many=True)
        serializer = serializers.ThreadSerializer(thread, many=True)

        return Response(serializer.data)

    def get_object(self):
        other_username  = self.kwargs.get("username")
        obj, created    = Thread.objects.get_or_new(self.request.user, other_username)
        if obj == None:
            raise Http404
        return obj

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        thread = self.get_object()
        print(thread)
        user = self.request.user
        message = self.request.data.get("message")
        message=ChatMessage.objects.create(user=user, thread=thread, message=message)
        serializer = serializers.MessageSerializer(message, many=True)
        return Response(serializer.data)

