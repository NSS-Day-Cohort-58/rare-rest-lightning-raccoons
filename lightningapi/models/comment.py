from django.db import models
from .post import Post
from django.contrib.auth.models import User


class Comments(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
