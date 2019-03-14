from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response  
from .serializers import TestSerializer,AirportSerializer
from .models import TestModel,AirportModel
import json
import requests
import os

airportKey = os.environ.get('airportKey')
airportAppId = os.environ.get('airportAppId')

class TestView(viewsets.ModelViewSet):      
    serializer_class = TestSerializer         
    queryset = TestModel.objects.all()  

def ListAirports(request):
    
    payload = (
        ('appId', '86201515'),
        ('appKey', 'd0224781a3d6153648f04251c97c3db7'),
        )
    response = requests.get('https://api.flightstats.com/flex/airports/rest/v1/json/active', params=payload)

    data = response.json()
    return JsonResponse(data)
    

            

# def airport_list(request):
#     r = requests.get(f'https://api.flightstats.com/flex/airports/rest/v1/json/active?appId={airportAppId}&appKey={airportKey}')
#     data = r.json()
#     return render(request, './templates/airports.html', {'data': json.dumps(data)})