from apps.detalle_ordenes.models import DetalleOrden
from rest_framework import serializers

class DetalleOrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleOrden
        fields = '__all__'