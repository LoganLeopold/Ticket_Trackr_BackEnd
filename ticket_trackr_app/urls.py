from django.urls import path
from . import views

urlpatterns = [
  path('', views.ListAirports),
  path('skyscan', views.simple_html_view)
]