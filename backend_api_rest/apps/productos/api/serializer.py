from apps.productos.models import Producto
from apps.detalle_ordenes.models import DetalleOrden
from rest_framework import serializers

class DetalleOrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleOrden
        fields = ['id', 'orden']

class ProductoSerializer(serializers.ModelSerializer):
    detalle_ordenes_producto = DetalleOrdenSerializer(many=True, read_only=True)
    class Meta:
        model = Producto
        fields = ['id','name','detalle_ordenes_producto', 'entry_date', 'stock', 'expiration_date', 'value', 'brand']
