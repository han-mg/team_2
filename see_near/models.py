from django.db import models

# Create your models here.
class blog_user(models.Model):
    id=models.TextField(max_length=100)
    password=models.TextField(max_length=200)
    nickname=models.TextField(max_length=200)
    user_name=models.TextField(max_length=200)
    email=models.EmailField(max_length=254)
    