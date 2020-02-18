from accounts import models
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.User
        fields = ('id','email','name','password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style': { 'input_type':'password'}
            }
        }
    def create(self,validated_data):
        user=models.User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password = validated_data['password'],

        )
        return user