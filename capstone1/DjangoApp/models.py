from django.db import models


# Create your models here.

class Person(models.Model):
    username = models.CharField(max_length=250)
    fullname = models.CharField(max_length=250)
    password = models.CharField(max_length=250)


class Processed(models.Model):
    col_name_word = models.CharField(max_length=250)
    col_name_pos = models.CharField(max_length=250)
    col_name_neg = models.CharField(max_length=250)
    col_name_acc = models.CharField(max_length=250)
    col_stop_word = models.CharField(max_length=250)
