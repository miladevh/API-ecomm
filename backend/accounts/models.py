from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager

class User(AbstractBaseUser):

    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'full_name']

    def __str__(self):
        return self.email
    
    # user permission
    def has_perm(self, perm, obj=None):
        return True
    
    # user have permissions to view the app
    def has_module_perms(self, app_label):
        return True
    
    # user is admin
    @property
    def is_staff(self):
        return self.is_admin


