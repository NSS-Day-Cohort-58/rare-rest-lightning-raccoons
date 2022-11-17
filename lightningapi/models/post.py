from django.db import models
from .category import Category
from lightningapi.models.rare_user import RareUser

class Post(models.Model):
    user = models.ForeignKey(RareUser, on_delete=models.CASCADE, related_name='post')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="post")
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
    image = models.CharField(max_length=255, null=True)
    content = models.TextField()
    approved = models.BooleanField()
