from rest_framework import serializers
from django.contrib.auth.models import User


class PostSerializer(serializers.Serializer):
    content = serializers.CharField()
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

