from apps.ingredientes.models import Ingrediente
from rest_framework import serializers

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'