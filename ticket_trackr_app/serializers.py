from rest_framework import serializers
from .models import TestModel, AirportModel, CountryModel

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirportModel
        fields = ("fs", "faa", "name", "city", "stateCode", "countryCode", "countryName", "regionName", "timeZoneRegionName", "localTime", "utcOffsetHours", "latitude", "longitude", "elevationFeet", "classification", "active", "weatherUrl", "delayIndexUrl")

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryModel
        fields = ('Code', 'Name')
