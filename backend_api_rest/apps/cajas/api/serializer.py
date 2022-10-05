from apps.cajas.models import Caja
from rest_framework import serializers

class CajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caja
        fields= '__all__'