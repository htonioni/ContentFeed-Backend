from rest_framework import serializers
from django.contrib.auth.models import User
from posts.models import Post


class PostSerializer(serializers.Serializer):
    content = serializers.CharField()
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def create(self,validated_data):
        import pdb; pdb.set_trace()
        return Post.objects.create(**validated_data)    