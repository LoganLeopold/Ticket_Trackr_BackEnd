from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework import viewsets, renderers, serializers
from rest_framework.response import Response
from .serializers import CountrySerializer, AirportSerializer   
from .models import  CountryModel, AirportModel
import json
import requests
import os

RAPID_KEY = os.environ.get("RAPIDAPI")
AVIATIONEDGE = os.environ.get("AVIATIONEDGE")

# ________ GENERAL __________ 
def apiHome(request):
    return JsonResponse('API Home', safe=False, content_type="text/html")

# ________ COUNTRY VIEWS __________ 
#Get API response
#countries/search/third
def CheckAPI(request):

    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/reference/v1.0/countries/en-US"

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': RAPID_KEY,
        }

    response = requests.request("GET", url, headers=headers)

    print(RAPID_KEY, "countries/search/third rapidapi key")
    data = response.json()
    return JsonResponse(data, safe=False, content_type='text/html')


#Put API results in DB
#countries/db/save
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
    #   country.save()

    return redirect('countrylist')
    # return JsonResponse(countreis_data, safe=False, content_type='text/html')


# simple country view to test database
#countries/db/search
def CountryList(request):
    countries = CountryModel.objects.all()
    serializer = CountrySerializer(countries, many=True)
    response = JsonResponse(serializer.data, safe=False, content_type='text/html')
    response["Access-Control-Allow-Origin"] = "http://localhost:3000"
    response["Access-Control-Allow-Oirign"] = ""
    return response 
    # return render(request, 'countries.html', {'countries': serializer.data})
    


# ________ AIRPORT VIEWS __________ 
#airports/search/third
def checkAirportAPI (request):

    url = 'https://aviation-edge.com/v2/public/airportDatabase?key=%s' % AVIATIONEDGE

    print(AVIATIONEDGE)

    response = requests.request("GET", url)

    airport_data = response.json()
    count = 0

    return JsonResponse(airport_data, safe=False, content_type='text/html')


#Put API results in DB
#airports/db/save
def saveAirports(request): 

    url = 'https://aviation-edge.com/v2/public/airportDatabase?key=%s   ' % AVIATIONEDGE

    response = requests.request("GET", url)

    airports_data = response.json()

    # airports = []
    # for airport in airports_data:
    #     airports.append(airport['nameAirport'])

    for airport in airports_data:
      airport = AirportModel.objects.create(
        Id=airport['airportId'],
        Name=airport['nameAirport'],
        IataCode=airport['codeIataAirport'],
        IcaoCode=airport['codeIcaoAirport'],
        CountryName=airport['nameCountry'],
        CountryCode=airport['codeIso2Country'],
        CityCode=airport['codeIataCity'],
      )

      airport.save()

    # return JsonResponse(airports_data, safe=False, content_type='text/html')
    return redirect('airportslist')

# simple airport view to test database
#airports/search/db
def AirportList(request):
    airports = AirportModel.objects.all()
    serializer = AirportSerializer(airports, many=True)
    response = JsonResponse(serializer.data, safe=False, content_type='text/html')
    response["Access-Control-Allow-Origin"] = "http://localhost:3000"
    return response