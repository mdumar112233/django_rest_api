from django.contrib import admin
from .models import StudentConcreteModel
# Register your models here.

@admin.register(StudentConcreteModel)
class StudentConcreteModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']
