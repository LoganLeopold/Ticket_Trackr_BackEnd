from django.contrib import admin
from .models import TestModel

class TestAdmin(admin.ModelAdmin):  # add this
      list_display = ('name', 'test',)

admin.site.register(TestModel, TestAdmin)
