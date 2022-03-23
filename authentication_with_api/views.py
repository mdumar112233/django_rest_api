from django.shortcuts import render
from rest_framework.response import Response
from .models import StudentAuthenticationModel
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from .custompermissions import MyPermission
# import throttling 
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle


from .throttlings import EmployeeUserRateThrottle


### CRUD WITH MODELVIEWSET ---------------------------
# class StudentAuthenticateModelViewSet(viewsets.ModelViewSet):
#     queryset = StudentAuthenticationModel.objects.all()
#     serializer_class = StudentSerializer

#     ### add basic authentication for crud
#     ### check setting for global set this authentication

#     authentication_classes = [BasicAuthentication]
#     # permission_classes = [IsAuthenticated]
#     permission_classes = [IsAdminUser]


# class StudentAuthenticateModelViewSet(viewsets.ModelViewSet):
#     queryset = StudentAuthenticationModel.objects.all()
#     serializer_class = StudentSerializer
    
#     #### overwrite global authentication
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [AllowAny]



####### SESSION AUTHENTICATION -------------------------

class StudentAuthenticateModelViewSet(viewsets.ModelViewSet):
    queryset = StudentAuthenticationModel.objects.all()
    serializer_class = StudentSerializer

    ### add basic authentication for crud
    ### check setting for global set this authentication

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]



    ### CUSTOM AUTHENTICATION
    # permission_classes = [MyPermission]



##### DJANGO THROTTLING -------------------------------


# class StudentAuthenticateModelViewSet(viewsets.ModelViewSet):
#     queryset = StudentAuthenticationModel.objects.all()
#     serializer_class = StudentSerializer

#     authentication_classes = [SessionAuthentication]
#     # permission_classes = [IsAuthenticated]
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     ### THROTTLE RATE SET IN GLOBALLY 
#     # throttle_classes = [AnonRateThrottle, UserRateThrottle]

#     throttle_classes = [AnonRateThrottle, EmployeeUserRateThrottle]



##### SET THROTTLING IN SINGLE CRUD REQUEST 

# class StudentList(ListAPIView):
#     queryset = StudentConcreteModel.objects.all()
#     serializer_class = StudentSerializer

#     throttle_classes = [ScopedRateThrottle]
#     throttle_scope = 'listview'

# class StudentCreate(CreateAPIView):
#     queryset = StudentConcreteModel.objects.all()
#     serializer_class = StudentSerializer

#     throttle_classes = [ScopedRateThrottle]
#     throttle_scope = 'createview'





