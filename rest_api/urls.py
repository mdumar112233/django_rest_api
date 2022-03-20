from django.urls import path
from . import views


urlpatterns = [
    path('getdata/', views.student_detail, name='student_detail'),
    path('alldata/', views.student_list, name='student_list'),
]

