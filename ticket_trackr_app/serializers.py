from rest_framework import serializers
from .models import TestModel, AirportModel, CountryModel

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirportModel
        fields = (
            'Id',
            'Name',
            'IataCode',
            'IcaoCode',
            'CountryName',
            'CountryCode',
            'CityCode',
        )

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryModel
        fields = ('Code', 'Name')


