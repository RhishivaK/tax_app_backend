from rest_framework import serializers
from autho.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'pan_number', 'password', 'role')

    def create(self, validated_data):
        user = User.create_user(validated_data)
        return user
    
    def update(self, instance, validated_data):
        instance.update(**validated_data)
        instance.save()
        return instance