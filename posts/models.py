from django.db import models

from users.models import User

class Post(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__ (instance):
        return f"{instance.content} ({instance.id})"