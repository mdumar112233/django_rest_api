from django.urls import path
from . import views

urlpatterns = [
    path('studentfilter/', views.StudentList.as_view(), name='studentlist')
]






