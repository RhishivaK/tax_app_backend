from autho.models import *
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import get_user_model
from django.utils import timezone

class UserManager(BaseUserManager):
    def _create_user(self, first_name, middle_name, last_name, email, phone_number, pan_number, password, role):
        email = self.normalize_email(email)
        user = self.model(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            pan_number=pan_number,
            role=role,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, first_name, middle_name, last_name, email, phone_number, pan_number, password, role):
        return self._create_user(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            pan_number=pan_number,
            password=password,
            role=role,
        )