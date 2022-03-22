from rest_framework import serializers
from .models import StudentJWTAuthenticationModel

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentJWTAuthenticationModel
        
        fields = ['id', 'name', 'roll', 'city']