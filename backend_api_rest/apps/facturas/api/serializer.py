from apps.facturas.models import Factura
from rest_framework import serializers

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'