from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import StudentConcreteModel
from .serializers import StudentSerializer

# Create your views here.

# class StudentList(ListAPIView):
#     queryset = StudentConcreteModel.objects.all()
#     serializer_class = StudentSerializer

# class StudentCreate(CreateAPIView):
#     queryset = StudentConcreteModel.objects.all()
#     serializer_class = StudentSerializer


# class StudentRetrive(RetrieveAPIView):
#     queryset = StudentConcreteModel.objects.all()
#     serializer_class = StudentSerializer


##### CUMBINE API VIEW

class StudentListCreate(ListCreateAPIView):
    queryset = StudentConcreteModel.objects.all()
    serializer_class = StudentSerializer

    
class StudentRetriveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = StudentConcreteModel.objects.all()
    serializer_class = StudentSerializer















