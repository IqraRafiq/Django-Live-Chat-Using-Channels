from rest_framework import serializers

from chating import models

class ThreadSerializer(serializers.ModelSerializer):
    """serialize profile feed item"""
    class Meta:
        model = models.Thread
        fields = ('id', 'first', 'second')
        extra_kwargs = {
            'first' : {
                'read_only':True
            },
            'second' : {
                'read_only':True
            },
        }
class MessageSerializer(serializers.ModelSerializer):
    """serialize profile feed item"""
    class Meta:
        model = models.ChatMessage
        fields = ('id', 'user', 'thread','message')
        extra_kwargs = {
            'user' : {
                'read_only':True
            },
            'thread' : {
                'read_only':True
            },
        }
class ChatSerializer(ThreadSerializer,MessageSerializer):
    ...