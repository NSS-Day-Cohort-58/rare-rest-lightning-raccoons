from django.db import models
from .post import Post
from .reaction import Reaction
from lightningapi.models.rare_user import RareUser

class Subscription(models.Model):
    follower = models.ForeignKey(RareUser, on_delete=models.CASCADE, related_name='follower')
    author = models.ForeignKey(RareUser, on_delete=models.CASCADE, related_name='author')
    created_on = models.DateTimeField()
