from django.db import models, transaction
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth import get_user_model
from autho.managers import *

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null = True, blank = True)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15)
    pan_number = models.IntegerField()
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=15)

    objects=UserManager()
    USERNAME_FIELD = 'email'
    class Meta:
        db_table = 'users'

    @classmethod
    @transaction.atomic
    def create_user(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user