from rest_framework import serializers
from .models import StudentFilterModel


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentFilterModel

        fields = ['id', 'name', 'roll', 'city', 'passby']



