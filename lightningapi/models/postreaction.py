from django.db import models
from .post import Post
from .reaction import Reaction
from lightningapi.models.rare_user import RareUser

class PostReaction(models.Model):
    reaction = models.ForeignKey(Reaction, on_delete=models.CASCADE)
    user = models.ForeignKey(RareUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
