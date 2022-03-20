from django.contrib import admin
from .models import Student_De_serialization

# Register your models here.

@admin.register(Student_De_serialization)
class Student_De_serialization_Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']
