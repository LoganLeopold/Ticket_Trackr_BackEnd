from django.contrib import admin
from .models import TestModel, CountryModel
# , AirportModel

class TestAdmin(admin.ModelAdmin):  
      list_display = ('name', 'test',)

class CountryAdmin(admin.ModelAdmin):
      list_display = ('Code', 'Name',)

class AirportAdmin(admin.ModelAdmin):
      list_display = ('Id','Name','IataCode','IcaoCode','CountryName','CountryCode','CityCode',)

admin.site.register(TestModel, TestAdmin)
admin.site.register(CountryModel, CountryAdmin)
# admin.site.register(AirportModel, AirportAdmin)