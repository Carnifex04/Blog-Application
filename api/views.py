from django.shortcuts import render
from rest_framework import generics
from api import serializers
from django.contrib.auth.models import User


# Create your views here.

# UserList view provides read-only access to the list of users
class UserList(generics.ListAPIView):
    # list of model instances
    queryset = User.objects.all()
    # serializes the User data
    serializer_class = serializers.UserSerializer


# UserDetail view provides read-only access to a single user.
class UserDetail(generics.RetrieveAPIView):
    # list of model instances
    queryset = User.objects.all()
    # serializes the User data
    serializer_class = serializers.UserSerializer
