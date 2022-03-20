from django.contrib import admin
from .models import Studentcrud
# Register your models here.

@admin.register(Studentcrud)
class StudentcrudAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']



