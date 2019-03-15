from django.urls import path
from . import views

urlpatterns = [
  path('search/', views.ListAirports),
#   path('skyscan', views.GetLivePrices),
#   path('skyscancollect', views.GetFormData)
]