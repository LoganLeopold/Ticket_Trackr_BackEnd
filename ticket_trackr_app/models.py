from django.db import models

# Create your models here.

class TestModel(models.Model):
    name = models.CharField(max_length=100)
    test = models.TextField()

class FlightGet(models.Model):
    inboundDate = models.CharField(max_length=10) 
    cabinClass = models.TextField()
    originPlace = models.TextField()
    destinationPlace = models.TextField()
    outboundDate = models.CharField(max_length=10)
    adults = models.CharField(max_length=1)
    # country = models.TextField()
    # currency = models.TextField()
