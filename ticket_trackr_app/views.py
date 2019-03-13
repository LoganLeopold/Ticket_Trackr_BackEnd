from django.shortcuts import render
from rest_framework import viewsets          
from .serializers import TestSerializer      
from .models import TestModel
import requests


class TestView(viewsets.ModelViewSet):      
    serializer_class = TestSerializer          
    queryset = TestModel.objects.all()  


# class AirportLIst(viewsets.ModelViewSet):
#     serializer_class = AirportSerializer

#     queryset = requests.get("https://api.flightstats.com/flex/airports/rest/v1/json/active?appId=86201515&appKey=d0224781a3d6153648f04251c97c3db7")

def airport_list(request):
    r = requests.get("https://api.flightstats.com/flex/airports/rest/v1/json/active?appId=86201515&appKey=d0224781a3d6153648f04251c97c3db7")
    data = r.json()
    return render(request, './templates/airports.html')