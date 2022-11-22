from django.db import models
from .tag import Tag
from .post import Post


class PostTag(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='post_tags')
    tag = models.ForeignKey(
        Tag, on_delete=models.CASCADE, related_name='post_tags')
