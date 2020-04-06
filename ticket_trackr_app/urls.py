from django.urls import path
from . import views

urlpatterns = [
  path('countries/search/third', views.CheckAPI),
  path('countries/db/save', views.saveCountries),
  path('countries/search/db', views.CountryList, name='countrylist'),

  path('airports/search/third', views.checkAirportAPI),
  path('airports/db/save', views.saveAirports),
  path('airports/search/db', views.AirportList, name='airportlist')
]





