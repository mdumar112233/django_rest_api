from django.urls import path
from . import views


urlpatterns = [
    # path('studentgenericapi/', views.StudentList.as_view()),
    # path('studentgenericapi/', views.StudentCreate.as_view()),

    # path('studentgenericapi/<int:pk>/', views.StudentRetrive.as_view()),

    # path('studentgenericapi/<int:pk>/', views.StudentUpdate.as_view()),

    # path('studentgenericapi/<int:pk>/', views.StudentDelete.as_view()),

    path('studentgetpost/', views.StudentGetPost.as_view()),

    path('studentgetpost/<int:pk>/', views.StudentRetriveUpdateDelete.as_view()),


]










