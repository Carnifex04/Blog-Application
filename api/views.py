from django.shortcuts import render
from rest_framework import generics
from api import serializers
from api.models import Post
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


# Creating a set of views for the Post API
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
