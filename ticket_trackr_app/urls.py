from django.urls import path
from . import views

urlpatterns = [
  path('', views.ListAirports),
#   path('skyscan', views.GetLivePrices),
#   path('skyscancollect', views.GetFormData)
]