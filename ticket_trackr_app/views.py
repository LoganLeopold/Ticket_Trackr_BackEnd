from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, StaticHTMLRenderer
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

def CountryList(request):
    countries = CountryModel.objects.all()
    return render(request, 'countries.html', {'countries': countries})

def StoreCountries(request):

    payload = {
        'X-RapidAPI-Key': RAPID_KEY,
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.get(
        'https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/reference/v1.0/countries/en-US', headers=payload)

    countries_data = response.json()

    for country in countries_data['Countries']:
        country = CountryModel.object.create(Name=country.Name, Code=country.Code)
    
    return redirect('countrylist')

    # return JsonResponse(countries_data, safe=False, content_type='text/html')
    

#    serialized_countries = CountrySerializer(data=countries_data['Countries'], many=True)
#     serialized_countries.is_valid(True)