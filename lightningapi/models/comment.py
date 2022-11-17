from django.db import models
from .post import Post
from lightningapi.models.rare_user import RareUser

class Comment(models.Model):
    author = models.ForeignKey(RareUser, on_delete=models.CASCADE, related_name='comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    content = models.TextField()
