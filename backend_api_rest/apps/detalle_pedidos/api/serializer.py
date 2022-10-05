from apps.detalle_pedidos.models import DetallePedido
from rest_framework import serializers

class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = '__all__'