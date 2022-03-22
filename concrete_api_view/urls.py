from django.urls import path
from . import views

urlpatterns = [
    # path('studentconcreteapi/', views.StudentList.as_view()),
    # path('studentconcreteapi/', views.CreateAPIView.as_view()),
    # path('studentconcreteapi/<int:pk>/', views.StudentRetrive.as_view()),


    path('studentconcreteapi/', views.StudentListCreate.as_view()),

    path('studentconcreteapi/<int:pk>/', views.StudentRetriveUpdateDestroy.as_view()),

] 










