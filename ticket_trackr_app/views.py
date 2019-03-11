from django.shortcuts import render
from rest_framework import viewsets          
from .serializers import TestSerializer      
from .models import TestModel


class TestView(viewsets.ModelViewSet):      
    serializer_class = TestSerializer          
    queryset = TestModel.objects.all()  
