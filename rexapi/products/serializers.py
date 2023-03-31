from rest_framework import serializers
from .models import *

class productserializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields =('__all__')

class locationserializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields =('__all__')