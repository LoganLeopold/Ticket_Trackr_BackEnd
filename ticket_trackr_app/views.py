from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TestSerializer, AirportSerializer
from .models import TestModel, AirportModel
import json
import requests
import os

airportKey = os.environ.get('airportKey')
airportAppId = os.environ.get('airportAppId')
SKY_SCAN = os.environ.get("SKY_SCAN_KEY")

class TestView(viewsets.ModelViewSet):
    serializer_class = TestSerializer
    queryset = TestModel.objects.all()


def ListAirports(request):

    payload = (
        ('appId', airportKey),
        ('appKey', airportAppId),
    )
    response = requests.get(
        'https://api.flightstats.com/flex/airports/rest/v1/json/active', params=payload)

    data = response.json()
    return JsonResponse(data)


def GetLivePrices(request):
    paylod = {
        "inboundDate": "2019-04-08",
        "cabinClass": "business",
        "children": 0,
        "infants": 0,
        "country": "US",
        "currency": "USD",
        "locale": "en-US",
        "originPlace": "SFO-sky",
        "destinationPlace": "LHR-sky",
        "outboundDate": "2019-04-04",
        "adults": 1
    }

    headers = {
        "X-RapidAPI-Key": "f{SKY_SCAN}",
        "Content-Type": "application/x-www-form-urlencoded"
    }


response = unirest.post("https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/v1.0",
