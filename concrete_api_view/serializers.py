from rest_framework import serializers
from .models import StudentConcreteModel

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentConcreteModel
        
        fields = ['id', 'name', 'roll', 'city']