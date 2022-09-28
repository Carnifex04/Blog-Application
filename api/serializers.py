# importing serializers and User module

from rest_framework import serializers
from django.contrib.auth.models import User
# imported Post Model
from api.models import Post


# UserSerializer class which inherits from the ModelSerializer class
class UserSerializer(serializers.ModelSerializer):
    # list of posts in this many-to-one relationship
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        # initializing model associated with this serializer
        model = User
        # initializing fields to be included in the serializer
        fields = ['id', 'username', 'first_name', 'last_name', 'posts']


# Serializing the Post model data
# PostSerializer class which inherits from the ModelSerializer class
class PostSerializer(serializers.ModelSerializer):
    # returns the username of the author
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author']
