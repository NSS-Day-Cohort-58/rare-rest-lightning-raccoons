from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.CharField(max_length=25)
    bio = models.TextField(max_length=255)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    profile_img_url = models.CharField(max_length=100, null=True)
    created_on = models.DateTimeField()
    active = models.BooleanField()
