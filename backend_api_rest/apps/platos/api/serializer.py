from apps.platos.models import Plato
from apps.ingredientes.models import Ingrediente
from apps.detalle_ordenes.models import DetalleOrden
from rest_framework import serializers

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['id', 'name']

class DetalleOrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleOrden
        fields = ['id', 'orden']

class PlatoSerializer(serializers.ModelSerializer):
    ingredientes = IngredienteSerializer(many=True, read_only=True)
    detalle_ordenes_plato = DetalleOrdenSerializer(many=True, read_only=True)

    class Meta:
        model = Plato
        fields = ['name', 'description', 'ingredientes', 'detalle_ordenes_plato']