from django.db import models

# Create your models here.

class CountryModel(models.Model):
    Code = models.CharField(max_length=2)
    Name = models.TextField()

class TestModel(models.Model):
    name = models.CharField(max_length=100)
    test = models.TextField()

class AirportModel(models.Model):
    Id = models.TextField(default="placeholder", null=True, blank=True)
    Name = models.TextField(default="placeholder", null=True, blank=True)
    IataCode = models.TextField(default="placeholder", null=True, blank=True)
    IcaoCode = models.TextField(default="placeholder", null=True, blank=True)
    CountryName = models.TextField(default="placeholder", null=True, blank=True)
    CountryCode = models.TextField(default="placeholder", null=True, blank=True)
    CityCode = models.TextField(default="placeholder", null=True, blank=True)


#____ Establishing DB Airports ____ 

#1 .The cities have airports in them, so build city model:
#-City Name
#-City IATA Code
#-Airports Array

#2. Get airports and programmatically add them to cities:
#-Get city objects
#-For each airport, if the city code is equal to a city IATA code record, relate the airport to the #City with a foreign key


