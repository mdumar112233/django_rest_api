from rest_framework import serializers
from .models import Student_De_serialization

class De_Serializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=50)
    roll = serializers.IntegerField()

    def create(self, validate_data):
        return Student_De_serialization.objects.create(**validate_data)