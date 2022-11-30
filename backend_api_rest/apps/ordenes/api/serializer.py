from apps.ordenes.models import Orden
from apps.boletas.models import Boleta
from rest_framework import serializers
from apps.detalle_ordenes.models import DetalleOrden

class DetalleOrdenSerializer(serializers.ModelSerializer):
    class Meta: 
        model = DetalleOrden
        fields = ['id', 'plato', 'producto', 'number_dish' ]

class BoletaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Boleta
        fields = ['id']

class OrdenSerializer(serializers.ModelSerializer):
    boletas = BoletaSerializer(many=True, read_only=True)
    detalle_ordenes = DetalleOrdenSerializer(many=True, read_only=True)
    class Meta:
        model = Orden
        fields = ['id', 'boletas', 'detalle_ordenes','start_time','end_time','mesa','date','number_people','state']