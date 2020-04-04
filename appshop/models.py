from django.db import models


class Product(models.Model):

    object = models.Manager()
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):

    object = models.Manager()
    name = models.CharField(max_length=255)
    price = models.FloatField()
    code = models.CharField(max_length=10)
    discription = models.CharField(max_length=255)
    discount = models.FloatField()
    image_url = models.CharField(max_length=2083)
# Create your models here.
