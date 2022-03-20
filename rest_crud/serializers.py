from rest_framework import serializers
from .models import Studentcrud

class StudentCreate(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()

    # POST METHOD OF REST API
    # POST DATA TO DATABASE
    def create(self, validated_data):
        return Studentcrud.objects.create(**validated_data)
    
    # UPDATE METHOD OF REST API
    # UPDATE DATA TO DATABASE
    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get('name', instance.name)
        print(instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)

        return instance

