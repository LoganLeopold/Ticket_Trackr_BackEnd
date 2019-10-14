from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework import viewsets, renderers, serializers
from rest_framework.response import Response
from .serializers import TestSerializer, AirportSerializer, CountrySerializer
from .models import TestModel, AirportModel, CountryModel
import json
import requests
import os

RAPID_KEY = os.environ.get("RAPIDAPI")

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

#Get API response
def CheckAPI(request):

    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/reference/v1.0/countries/en-US"

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': RAPID_KEY,
        }

    response = requests.request("GET", url, headers=headers)

    print(RAPID_KEY)
    data = response.json()
    return JsonResponse(data, safe=False, content_type='text/html')


#Put API results in DB
def saveCountries(request): 

    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/reference/v1.0/countries/en-US"

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': RAPID_KEY,
        }

    response = requests.request("GET", url, headers=headers)

    # serializer = CountrySerializer(query, many=True)

    # for country in serializer.data:
    #     print(country['Code'])

    countries_data = response.json()

    for country in countries_data['Countries']:
        print(country['Code'])

    for country in countries_data['Countries']:
      country = CountryModel.objects.create(Name=country['Name'], Code=country['Code'])
      country.save()

    return redirect('countrylist')
    # return JsonResponse(countreis_data, safe=False, content_type='text/html')
    
