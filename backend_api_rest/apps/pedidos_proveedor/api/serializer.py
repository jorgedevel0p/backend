from apps.pedidos_proveedor.models import PedidoProveedor
from rest_framework import serializers

class PedidoProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoProveedor
        fields = '__all__'