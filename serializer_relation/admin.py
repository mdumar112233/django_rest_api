from django.contrib import admin
from .models import Singer, Song

# Register your models here.

@admin.register(Singer)
class NewSerializerSingerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender']


@admin.register(Song)
class NewSerializerSongAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'duration', 'singer']










