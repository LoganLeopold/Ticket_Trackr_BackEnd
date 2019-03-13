from rest_framework import serializers
from .models import TestModel

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = ('name', 'test')

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirportModel