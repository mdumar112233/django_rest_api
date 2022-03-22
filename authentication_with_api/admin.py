from django.contrib import admin
from .models import StudentAuthenticationModel
# Register your models here.

@admin.register(StudentAuthenticationModel)
class StudentViewsetModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']
