from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from .models import StudentGenericApiModel

# Create your views here.

#### SINGLE GENERIC API VIEW WITH MODEL MIXIN
# class StudentList(GenericAPIView, ListModelMixin):
#     queryset = StudentGenericApiModel.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

# class StudentCreate(GenericAPIView, CreateModelMixin):
#     queryset = StudentGenericApiModel.objects.all()
#     serializer_class = StudentSerializer

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class StudentRetrive(GenericAPIView, RetrieveModelMixin):
#     queryset = StudentGenericApiModel.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# class StudentUpdate(GenericAPIView, UpdateModelMixin):
#     queryset = StudentGenericApiModel.objects.all()
#     serializer_class = StudentSerializer

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

# class StudentDelete(GenericAPIView, DestroyModelMixin):
#     queryset = StudentGenericApiModel.objects.all()
#     serializer_class = StudentSerializer

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


#### WITH ONE CLASS ALL GENERIC API VIEW WITH MODEL MIXIN

class StudentGetPost(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = StudentGenericApiModel.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 

class StudentRetriveUpdateDelete(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = StudentGenericApiModel.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)





















