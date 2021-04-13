from django.db import models


# Create your models here.

class Person(models.Model):
    username = models.CharField(max_length=250)
    fullname = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
