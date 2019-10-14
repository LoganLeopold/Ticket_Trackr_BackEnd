from django.urls import path
from . import views

urlpatterns = [
  path('search/', views.CountryList, name='countrylist'),
  path('search/all', views.CheckAPI),
  path('db/test', views.saveCountries),
]

