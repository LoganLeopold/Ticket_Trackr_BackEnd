"""ticket_trackr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import re_path
from django.views.generic.base import TemplateView
from rest_framework import routers                    
from ticket_trackr_app import views   
from django.conf import settings

react_routes = getattr(settings, 'REACT_ROUTES', [])


router = routers.DefaultRouter()                    
router.register(r'test', views.TestView, 'test')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # re_path(r'^.*/', TemplateView.as_view(template_name="base-react.html"), name='base'),
    path('airports/', include('ticket_trackr_app.urls')),    
]

# for route in react_routes:
#     urlpatterns += [
#         path('{}'.format(route), TemplateView.as_view(template_name='index.html'))
#     ]
