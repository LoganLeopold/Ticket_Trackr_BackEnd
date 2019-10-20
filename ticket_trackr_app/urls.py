from django.urls import path
from . import views

urlpatterns = [
  path('countries/search/', views.CountryList, name='countrylist'),
  path('countries/search/all', views.CheckAPI),
  path('countries/db/test', views.saveCountries),

  path('airports/search/', views.checkAirportAPI),
]

