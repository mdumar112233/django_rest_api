from django.contrib import admin
from .models import StudentGenericApiModel
# Register your models here.

@admin.register(StudentGenericApiModel)
class GenericApiView(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']

