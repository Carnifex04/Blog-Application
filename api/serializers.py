# importing serializers and User module

from rest_framework import serializers
from django.contrib.auth.models import User


# UserSerializer class which inherits from the ModelSerializer class
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # initializing model associated with this serializer
        model = User
        # initializing fields to be included in the serializer
        fields = ['id', 'username', 'first_name', 'last_name']
