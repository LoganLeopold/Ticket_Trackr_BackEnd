from django.db import models

# Create your models here.

class CountryModel(models.Model):
    Code = models.CharField(max_length=2)
    Name = models.TextField()

class TestModel(models.Model):
    name = models.CharField(max_length=100)
    test = models.TextField()

# class FlightGet(models.Model):
#     inboundDate = models.CharField(max_length=10) 
#     cabinClass = models.TextField()
#     originPlace = models.TextField()
#     destinationPlace = models.TextField()
#     outboundDate = models.CharField(max_length=10)
#     adults = models.CharField(max_length=1)
    # country = models.TextField()
    # currency = models.TextField()

class AirportModel(models.Model):
   fs = models.TextField(),
   faa = models.TextField(),
   name = models.TextField(),
   city = models.TextField(),
   stateCode = models.TextField(),
   countryCode = models.TextField(),
   countryName = models.TextField(),
   regionName = models.TextField(),
   timeZoneRegionName = models.TextField(),
   localTime = models.DateTimeField(),
   utcOffsetHours = models.IntegerField(),
   latitude = models.FloatField(),
   longitude = models.FloatField(),
   elevationFeet = models.IntegerField(),
   classification = models.IntegerField(),
   active = models.BooleanField(),
   weatherUrl = models.URLField(),
   delayIndexUrl = models.URLField()

# class AEAirportModel(models.model):
#     airportId: 
#     nameAirport: 
#     codeIataAirport: 
#     codeIcaoAirport: 
#     latitudeAirport: 
#     longitudeAirport: 
#     geonameId: 
#     timezone: 
#     GMT: 
#     phone: 
#     nameCountry: 
#     codeIso2Country: 
#     codeIataCity: 
