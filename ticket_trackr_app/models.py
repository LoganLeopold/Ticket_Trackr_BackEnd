from django.db import models

# Create your models here.

class CountryModel(models.Model):
    Code = models.CharField(max_length=2)
    Name = models.TextField()

class TestModel(models.Model):
    name = models.CharField(max_length=100)
    test = models.TextField()

class AirportModel(models.Model):
    Id = models.IntegerField(),
    Name = models.TextField(),
    IataCode = models.TextField(),
    IcaoCode = models.TextField(),
    CountryName = models.TextField(),
    CountryCode = models.TextField(),
    CityCode = models.TextField(),




#    fs = models.TextField(),
#    localTime = models.DateTimeField(),
#    utcOffsetHours = models.IntegerField(),
#    latitude = models.FloatField(),
#    active = models.BooleanField(),
#    delayIndexUrl = models.URLField()
