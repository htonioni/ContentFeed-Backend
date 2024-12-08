from rest_framework import serializers
from posts.models import Post
from users.models import User


class PostSerializer(serializers.Serializer):
    content = serializers.CharField()
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def create(self,validated_data):
        return Post.objects.create(**validated_data)    