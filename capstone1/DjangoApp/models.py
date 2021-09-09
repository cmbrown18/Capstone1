from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Person(models.Model):
    username = models.CharField(max_length=250, primary_key=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

    @property
    def get_username(self):
        return self.username

    @property
    def get_password(self):
        return self.password

    @property
    def get_Person(self):
        if Person.get_username == self.username:
            return self


class Processed(models.Model):
    col_name_word = models.CharField(max_length=250, primary_key=True)
    col_name_pos = models.CharField(max_length=250)
    col_name_neg = models.CharField(max_length=250)
    col_name_acc = models.CharField(max_length=250)
    col_stop_word = models.CharField(max_length=250)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=250)
