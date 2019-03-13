from django.db import models

# Create your models here.

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
    {
 "airports": [
  {
   fs = "00M",
   faa = "00M",
   name = "Thigpen",
   city = "Bay Springs",
   stateCode = "MS",
   countryCode = "US",
   countryName = "United States",
   regionName = "North America",
   timeZoneRegionName = "America/Chicago",
   localTime = "2019-03-13T08:06:48.605",
   utcOffsetHours = -5,
   latitude = 31.987639,
   longitude = -89.245056,
   elevationFeet = 351,
   classification = 5,
   active = true,
   weatherUrl = "https://api.flightstats.com/flex/weather/rest/v1/json/all/00M?codeType=fs",
   delayIndexUrl = "https://api.flightstats.com/flex/delayindex/rest/v1/json/airports/00M?codeType=fs"
  },


