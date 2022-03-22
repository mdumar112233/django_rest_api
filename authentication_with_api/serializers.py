from rest_framework import serializers
from .models import StudentAuthenticationModel

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAuthenticationModel
        
        fields = ['id', 'name', 'roll', 'city']