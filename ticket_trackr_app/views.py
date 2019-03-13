from django.shortcuts import render
from rest_framework import viewsets          
from .serializers import TestSerializer      
from .models import TestModel
import requests


class TestView(viewsets.ModelViewSet):      
    serializer_class = TestSerializer          
    queryset = TestModel.objects.all()  



def airport_list(request):
    r = requests.get()
    data = r.json()
    return render(request, './templates/airports.html')