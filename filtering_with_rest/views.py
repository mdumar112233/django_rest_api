from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import StudentFilterModel
from .serializers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.


class StudentList(ListAPIView):
    queryset = StudentFilterModel.objects.all()
    serializer_class = StudentSerializer

    ## DJANGO FILTER
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['city'] 

    # def get_queryset(self):
    #     user = self.request.user
    #     return StudentFilterModel.objects.filter(passby=user)


    #### SEARCH FILTER
    # filter_backends = [SearchFilter]
    # search_fields = ['city']

    # search_fields = ['^name']
    # search_fields = ['=name']
    

    ##### ORDERING FILTER 
    filter_backends = [OrderingFilter]
    ordering_fields = ['city']










