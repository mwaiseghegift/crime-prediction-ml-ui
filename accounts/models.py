from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True)
    is_admin = models.BooleanField(default=False)
    is_police = models.BooleanField(default=False)
    is_citizen = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name_plural = 'Users'
        db_table = 'users'
        