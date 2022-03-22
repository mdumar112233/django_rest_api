from django.contrib import admin
from .models import StudentViewsetModel
# Register your models here.

@admin.register(StudentViewsetModel)
class StudentViewsetModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']
