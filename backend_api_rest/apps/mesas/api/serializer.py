from apps.mesas.models import Mesa
from rest_framework import serializers

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = '__all__'
        