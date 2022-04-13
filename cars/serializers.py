from rest_framework import serializers
from .models import Car 

class CarSerializer(serializer.ModelSerializer):
    class Meta:
        model = Car 
        fields = ['id', 'make', 'model', 'price']