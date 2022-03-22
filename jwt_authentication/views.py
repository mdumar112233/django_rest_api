from django.shortcuts import render
from rest_framework.response import Response
from .models import StudentJWTAuthenticationModel
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

### CRUD WITH MODELVIEWSET ---------------------------

#### CREATE TOKEN WITH TARMINAL WITH THIS COMMAND
# python3 manage.py drf_create_token umar

class StudentAuthenticateModelViewSet(viewsets.ModelViewSet):
    queryset = StudentJWTAuthenticationModel.objects.all()
    serializer_class = StudentSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
  



