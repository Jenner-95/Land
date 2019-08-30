from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    telephone = models.IntegerField()
    email = models.EmailField(unique=True)
    PERMISSIONS= (
        ('0', 'Collaborator'),
        ('1', 'Administrator'),
    )
    permissions = models.CharField(max_length=1, choices=PERMISSIONS, blank=True, default='0')
    photo = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
