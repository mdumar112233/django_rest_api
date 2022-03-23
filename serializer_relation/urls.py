from django.db import router
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('singer', views.SingerViewSet, basename='singer')
router.register('song', views.SongViewSet, basename='song')


urlpatterns = [
    path('', include(router.urls)), 
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]

