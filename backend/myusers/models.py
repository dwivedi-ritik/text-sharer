from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from myusers.manager import MyUserManager
# Create your models here.


class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=60, unique=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',
                       'first_name', 'last_name']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_superuser
