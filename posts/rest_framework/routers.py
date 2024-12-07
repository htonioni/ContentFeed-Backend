from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.rest_framework.viewsets import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
# router.register(r'users', views.UserViewSet, basename='user')
