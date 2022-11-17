from django.db import models
from django.contrib.auth.models import User


class RareUser(models.Model):
    bio = models.TextField(max_length=255)
    profile_img_url = models.CharField(max_length=100, null=True)
    created_on = models.DateTimeField()
    active = models.BooleanField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

