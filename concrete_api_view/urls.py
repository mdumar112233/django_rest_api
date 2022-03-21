from django.urls import path
from . import views

urlpatterns = [
    path('studentconcreteapi/', views.StudentList.as_view()),
]










