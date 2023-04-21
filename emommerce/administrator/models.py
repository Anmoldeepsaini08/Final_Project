from django.db import models
from distutils.command.upload import upload

from unicodedata import category
# Create your models here.

class Items(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    quantity = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/',null=True)

class users(models.Model):

    user_name = models.CharField(max_length=20)
    user_email = models.CharField(max_length=20)
    user_phone = models.IntegerField()
    user_pass = models.CharField(max_length=20)


class Cart(models.Model):

    user_email = models.CharField(max_length=20)
    user_item = models.CharField(max_length=20) 
    item_quantity = models.IntegerField(default=1)



