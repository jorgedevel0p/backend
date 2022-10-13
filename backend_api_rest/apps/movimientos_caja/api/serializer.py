from apps.movimientos_caja.models import MovimientoCaja
from rest_framework import serializers

class MovimientoCajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimientoCaja
        fields = '__all__'