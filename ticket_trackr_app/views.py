from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework import viewsets, renderers, serializers
from rest_framework.response import Response
from .serializers import AirportSerializer, CountrySerializer
from .models import AirportModel, CountryModel
import json
import requests
import os

RAPID_KEY = os.environ.get("RAPIDAPI")
AVIATIONEDGE = os.environ.get("AVIATIONEDGE")


# ________ COUNTRY VIEWS __________ 

# simple country view to test database
def CountryList(request):
    countries = CountryModel.objects.all()
    serializer = CountrySerializer(countries, many=True)
    response = JsonResponse(serializer.data, safe=False, content_type='text/html')
    response["Access-Control-Allow-Origin"] = "http://localhost:3000"
    return response 
    # return render(request, 'countries.html', {'countries': serializer.data})



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

    countries_data = response.json()

    for country in countries_data['Countries']:
        print(country['Code'])

    for country in countries_data['Countries']:
      country = CountryModel.objects.create(Name=country['Name'], Code=country['Code'])
      country.save()

    return redirect('countrylist')
    # return JsonResponse(countreis_data, safe=False, content_type='text/html')
    


# ________ AIRPORT VIEWS __________ 

def checkAirportAPI (request):

    url = 'https://aviation-edge.com/v2/public/airportDatabase?key=f72fb6-fa98fc'

    # headers = {
    #     'x-rapidapi-host': "montanaflynn-Airports-v1.p.rapidapi.com",
    #     'x-rapidapi-key': RAPID_KEY,
    #     }

    response = requests.request("GET", url)
    # , headers=headers)

    airport_data = response.json()
    count = 0

    for airport in airport_data:
        if count <= 100:
            print(airport['nameCountry'])
            count += 1

    oneairport = airport_data[0]['nameCountry']

    print(oneairport)

    return JsonResponse(oneairport, safe=False, content_type='text/html')