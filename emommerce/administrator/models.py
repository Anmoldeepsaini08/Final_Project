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
    item_size = models.CharField(max_length=9,default='Small') 

class Address(models.Model):

    user_email= models.CharField(max_length=20)
    user_address = models.CharField(max_length=70,default='N/A')
    user_pincode  = models.IntegerField(default=000000)


class Orders(models.Model):

    order_number = models.AutoField
    user_email = models.CharField(max_length=20)
    user_item = models.CharField(max_length=20) 
    item_quantity = models.IntegerField(default=1)
    item_size = models.CharField(max_length=9) 
    date =  models.CharField(max_length=20) 
    user_total = models.IntegerField()




