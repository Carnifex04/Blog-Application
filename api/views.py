from django.shortcuts import render
from rest_framework import generics
from api import serializers
from api.models import Post
from rest_framework import permissions
from api.permissions import OwnerAuthentication
from django.contrib.auth.models import User


# Create your views here.

# Home Page
def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'api/home.html', context)


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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, OwnerAuthentication]
