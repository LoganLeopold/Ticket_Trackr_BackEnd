from django.db import models

# Create your models here.

class CountryModel(models.Model):
    Code = models.CharField(max_length=2)
    Name = models.TextField()

class TestModel(models.Model):
    name = models.CharField(max_length=100)
    test = models.TextField()

class AirportModel(models.Model):
    Id = models.TextField(default="placeholder")
    Name = models.TextField(default="placeholder")
    IataCode = models.TextField(default="placeholder")
    IcaoCode = models.TextField(default="placeholder")
    CountryName = models.TextField(default="placeholder")
    CountryCode = models.TextField(default="placeholder")
    CityCode = models.TextField(default="placeholder")


