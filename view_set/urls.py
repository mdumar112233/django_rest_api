from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# createing router object
router = DefaultRouter()

# Register studnetviewset with router
router.register('studentviewsetapi', views.StudentReadOnlyModelViewSet, basename='student')


urlpatterns = [
    path('', include(router.urls))
]






