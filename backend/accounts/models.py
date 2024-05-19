from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
from django.db.models.signals import post_save

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
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    address = models.TextField(null=True, blank=True)
    birth_date = models.DateField()
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    balance = models.IntegerField(default=1000)

    def __str__(self):
        return self.user.email
    

def create_profile(sender, **kwargs):
    if kwargs['created']:
        UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(receiver=create_profile, sender=User)

