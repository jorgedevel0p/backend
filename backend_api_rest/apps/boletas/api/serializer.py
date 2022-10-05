from apps.boletas.models import Boleta
from rest_framework import serializers

class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleta
        fields = '__all__'