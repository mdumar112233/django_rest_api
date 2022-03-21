from wsgiref.validate import validator
from rest_framework import serializers
from .models import Studentcrud


##### REGULAR NORMAL SERIALIZER ------------------------------
 
# validators
# def start_with_r(value):
#     if  value[0].lower() != 'r':
#         raise serializers.ValidationError('Name must be start with R')

# class StudentCreateSerializer(serializers.Serializer):
#     # id = serializers.IntegerField()
#     name = serializers.CharField(max_length=100, validators=[start_with_r])

#     city = serializers.CharField(max_length=100)
#     roll = serializers.IntegerField()


#     # POST METHOD OF REST API
#     # POST DATA TO DATABASE
#     def create(self, validated_data):
#         return Studentcrud.objects.create(**validated_data)
    
#     # UPDATE METHOD OF REST API
#     # UPDATE DATA TO DATABASE
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.roll = validated_data.get('roll', instance.roll)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()

#         return instance


#     ### FIELD LEVEL VALIDATION
#     def validate_roll(self, value):
#         if value >= 200:
#             raise serializers.ValidationError('seat full')
#         return value

#     ### OBJECT LEVEL VALIDATION
#     def validate(self, data):
#         nm = data.get('name')
#         ct = data.get('city')

#         if nm.lower() == 'faruk khan' and ct.lower() != 'comilla':
#             raise serializers.ValidationError('City of comilla only allowed')
#         return data



##### MODEL SERIALIZER ------------------------------ 

class StudentCreateSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    class Meta:
        model = Studentcrud
        
        fields = ['name', 'roll', 'city']

        read_only_fields = ['name', 'roll']
        extra_kwargs = {'name': {'read_only': True}}




















