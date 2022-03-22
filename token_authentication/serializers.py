from rest_framework import serializers
from .models import StudentTokenAuthenticationModel

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTokenAuthenticationModel
        
        fields = ['id', 'name', 'roll', 'city']