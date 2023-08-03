from django.db import models

# Create your models here.
class seenear_user(models.Model):
    user_id=models.TextField(max_length=100)
    password=models.TextField(max_length=200)
    nickname=models.TextField(max_length=200)
    user_name=models.TextField(max_length=200)
    email=models.EmailField(max_length=254)
    address=models.TextField(max_length=200)
    user_number=models.TextField(max_length=200)
    reg_date=models.DateTimeField(auto_now_add=True)