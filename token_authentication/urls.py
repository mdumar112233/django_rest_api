from django.db import router
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .auth import CustomAuthToken

router = DefaultRouter()

router.register('studentauthtoken', views.StudentAuthenticateModelViewSet, basename='student')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),

    # path('gettoken_auth/', CustomAuthToken.as_view())
]



