from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework import viewsets, renderers, serializers
from rest_framework.response import Response
from .serializers import TestSerializer, AirportSerializer, CountrySerializer
from .models import TestModel, AirportModel, CountryModel
import json
import requests
import os

RAPID_KEY = os.environ.get('RAPID')


class TestView(viewsets.ModelViewSet):
    serializer_class = TestSerializer
    queryset = TestModel.objects.all()

class CountryView(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = CountryModel.objects.all()

# simple country view to test database
def CountryList(request):
    countries = CountryModel.objects.all()
    return render(request, 'countries.html', {'countries': countries})

# put countries in the database upon deployment
# def StoreCountries(request):

#     payload = {
#         'X-RapidAPI-Key': RAPID_KEY,
#         'Content-Type': 'application/x-www-form-urlencoded'
#     }

#     response = requests.get(
#         'https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/reference/v1.0/countries/en-US', headers=payload)

#     countries_data = response.json()

#     for country in countries_data['Countries']:

#     for country in countries_data['Countries']:
#         country = CountryModel.objects.create(Name=country['Name'], Code=country['Code'])
    
#     return redirect('countrylist')

    # return JsonResponse(countries_data, safe=False, content_type='text/html')

# Update database every day
def CheckAPI(request):

    payload = {
        'X-RapidAPI-Key': RAPID_KEY,
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.get(
        'https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/reference/v1.0/countries/en-US', headers=payload)

    countries_data = response.json()

    query = CountryModel.objects.all()

    serializer = CountrySerializer(query, many=True)

    for country in countries_data['Countries']:
        print(country['Code'])

    for country in serializer.data:
        print(country['Code'])

    return JsonResponse(serializer.data, safe=False, content_type='text/html')
    

