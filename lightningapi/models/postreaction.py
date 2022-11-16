from django.db import models
from .post import Post
from .reaction import Reaction
from django.contrib.auth.models import User
class PostReaction(models.Model):
    reaction = models.ForeignKey(Reaction, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)