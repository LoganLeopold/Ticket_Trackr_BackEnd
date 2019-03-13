from django.urls import path
from . import views

urlpatterns = [
  path('', views.airport_list, name='airport_list'),

]