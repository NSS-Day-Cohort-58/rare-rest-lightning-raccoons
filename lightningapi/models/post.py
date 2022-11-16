from django.db import models
from .category import Category
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
    image = models.CharField(max_length=255, null=True)
    content = models.TextField()
    approved = models.BooleanField()
