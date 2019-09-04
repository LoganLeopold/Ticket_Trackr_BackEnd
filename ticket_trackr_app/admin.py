from django.contrib import admin
from .models import TestModel, CountryModel

class TestAdmin(admin.ModelAdmin):  
      list_display = ('name', 'test',)

class CountryAdmin(admin.ModelAdmin):
      list_display = ('Code', 'Name',)

admin.site.register(TestModel, TestAdmin)
admin.site.register(CountryModel, CountryAdmin)