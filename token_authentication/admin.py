from django.contrib import admin
from .models import StudentTokenAuthenticationModel

# Register your models here.

@admin.register(StudentTokenAuthenticationModel)
class StudentViewsetModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']
