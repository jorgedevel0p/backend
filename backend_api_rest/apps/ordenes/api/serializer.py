from apps.ordenes.models import Orden
from apps.boletas.models import Boleta
from rest_framework import serializers

class BoletaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Boleta
        fields = ['id']

class OrdenSerializer(serializers.ModelSerializer):
    boletas = BoletaSerializer(many=True, read_only=True)
    class Meta:
        model = Orden
        fields = ['id', 'boletas']