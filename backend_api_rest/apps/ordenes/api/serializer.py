from apps.ordenes.models import Orden
from rest_framework import serializers

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'