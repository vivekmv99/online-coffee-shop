# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class reg(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        db_table = "reg"

# Create your models here.
class register(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    class Meta:
        db_table = "register"

class items(models.Model):
    item_name = models.CharField(max_length=50)
    item_dis = models.CharField(max_length=50)
    item_price = models.IntegerField()
    pic=models.ImageField(upload_to='cafeapp/static/pics')
    path = models.CharField(max_length=50)
    class Meta:
        db_table = "items"

class order(models.Model):
    usname = models.CharField(max_length=50)
    it_name = models.CharField(max_length=50)
    it_price = models.IntegerField()
    it_quantity = models.IntegerField()
    it_totl = models.IntegerField()

    class Meta:
        db_table = "order"
