from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Estate(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    departament = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/', blank=True)

    def __str__(self):
        return self.name


class Plot(models.Model):
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tree(models.Model):
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE)
    diameter = models.IntegerField()
    height = models.IntegerField()
    health = models.CharField(max_length=50)
    year = models.CharField(max_length=50)

    def __str__(self):
        return self.Plot.name + " " + self.diameter