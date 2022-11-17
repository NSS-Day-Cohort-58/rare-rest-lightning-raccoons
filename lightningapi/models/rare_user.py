from django.db import models
from django.contrib.auth.models import User


class RareUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    bio = models.TextField(max_length=255)
    profile_img_url = models.CharField(max_length=100, null=True)

