from rest_framework import viewsets
from posts.models import Post
from posts.rest_framework.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]