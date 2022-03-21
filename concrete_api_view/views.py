from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import StudentConcreteModel
from .serializers import StudentSerializer

# Create your views here.

class StudentList(ListAPIView):
    queryset = StudentConcreteModel.objects.all()
    serializer_class = StudentSerializer

