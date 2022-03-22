from rest_framework import serializers
from .models import StudentViewsetModel

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentViewsetModel
        
        fields = ['id', 'name', 'roll', 'city']