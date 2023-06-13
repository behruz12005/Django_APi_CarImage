from rest_framework import serializers
from .models import GetCarImage

class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetCarImage
        fields = '__all__'