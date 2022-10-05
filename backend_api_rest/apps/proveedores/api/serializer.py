from apps.proveedores.models import Proveedor
from rest_framework import serializers

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'