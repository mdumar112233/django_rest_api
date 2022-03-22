from functools import partial
from django.shortcuts import render
from rest_framework.response import Response
from .models import StudentViewsetModel
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets

# Create your views here.

###### VIEW SET CLASS
class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        print('basename', self.basename)
        print('action', self.action)
        print('detail', self.detail)
        print('suffix', self.suffix)
        print('name', self.name)

        stu = StudentViewsetModel.objects.all()
        serializer = StudentSerializer(stu, many=True)

        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        id = pk
        stu = StudentViewsetModel.objects.get(pk=id)
        serializer = StudentSerializer(stu)

        return Response(serializer.data)
    
    def create(self, request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data create'}
            return Response(res)

        return Response(serializer.errors)

    def update(self, request, pk=None):
        id = pk
        stu = StudentViewsetModel.objects.get(pk=id)
        serializer = StudentSerializer(stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data Update'}
            return Response(res)

        return Response(serializer.errors)
    
    def partial_update(self, request, pk=None):
        id = pk
        stu = StudentViewsetModel.objects.get(pk=id)
        serializer = StudentSerializer(stu, data = request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data partial Update'}
            return Response(res)

        return Response(serializer.errors)
    
    def destory(self, request, pk=None):
        id = pk
        stu = StudentViewsetModel.objects.get(pk=id)
        stu.delete()
        res = {'msg': 'data delete'}
        return Response(res)


###### MODEL VIEW SET CLASS

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = StudentViewsetModel.objects.all()
    serializer_class = StudentSerializer


class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StudentViewsetModel.objects.all()
    serializer_class = StudentSerializer


