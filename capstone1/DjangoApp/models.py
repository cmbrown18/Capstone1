from django.contrib.auth.base_user import (AbstractBaseUser, BaseUserManager)
from django.db import models


# Create your models here.

class User(AbstractBaseUser):
    username = models.CharField(verbose_name='username',
                                max_length=200,
                                unique=True
                                )
    first_name = models.CharField(verbose_name='first name',
                                  max_length=200,
                                  unique=False)
    last_name = models.CharField(verbose_name='last name',
                                 max_length=200,
                                 unique=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def get_username(self):
        return self.username

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name


def set_name(user, first, last):
    user.first_name = first
    user.last_name = last


class Processed(models.Model):
    col_name_word = models.CharField(max_length=250, primary_key=True)
    col_name_pos = models.CharField(max_length=250)
    col_name_neg = models.CharField(max_length=250)
    col_name_acc = models.CharField(max_length=250)
    col_stop_word = models.CharField(max_length=250)
