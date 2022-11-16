from django.db import models
from .post import Post
from .reaction import Reaction
from django.contrib.auth.models import User
class Subscription(models.Model):
    follower = models.OneToOneField(User, on_delete=models.CASCADE)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField()