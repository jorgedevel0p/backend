from apps.platos.models import Plato
from apps.ingredientes.models import Ingrediente
from rest_framework import serializers

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['id', 'name']

class PlatoSerializer(serializers.ModelSerializer):
    ingredientes = IngredienteSerializer(many=True, read_only=True)

    class Meta:
        model = Plato
        fields = ['name', 'description', 'ingredientes']