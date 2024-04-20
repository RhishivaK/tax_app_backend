from django.db import models, transaction
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from users.managers import UserManager

class User(AbstractBaseUser):
    ROLE_CHOICES = [
        ('general', 'General User'),
        ('officer', 'Government Officer'),
        ('super_admin', 'Super Admin')
    ]

    MARITIAL_STATUS_CHOICES = [
        ('unmarried', 'Unmarried'),
        ('married', 'Married'),
        ('divorced', 'Divorced')
    ]
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null=True, blank=True, default='')
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=15)
    pan = models.CharField(max_length=100, unique=True)
    is_staff = models.BooleanField(default=False)
    password = models.CharField(max_length=100)
    maritial_status = models.CharField(max_length=20, choices=MARITIAL_STATUS_CHOICES)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='general')
    reward_points = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    objects = UserManager()
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'pan']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def has_module_perms(self, app_label): return True

    def has_perm(self, app_label): return True

    class Meta:
        db_table = 'auth_users'


