from django.contrib import admin
from .models import StudentJWTAuthenticationModel

# Register your models here.

@admin.register(StudentJWTAuthenticationModel)
class StudentViewsetModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']
