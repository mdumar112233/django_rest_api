from django.contrib import admin
from .models import StudentFilterModel

# Register your models here.

@admin.register(StudentFilterModel)
class StudentFilterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city', 'passby']

