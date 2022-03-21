from rest_framework import serializers
from .models import StudentGenericApiModel


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGenericApiModel
        fields = ['id', 'name', 'roll', 'city']





