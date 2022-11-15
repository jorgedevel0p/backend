from apps.mesas.models import Mesa
from rest_framework import serializers
from apps.reservas.models import Reserva

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id','status','date','time', 'date_reserva']

class MesaSerializer(serializers.ModelSerializer):
    reservas_mesa = ReservaSerializer(many=True, read_only=True)
    class Meta:
        model = Mesa
        fields = ['id', 'number_name', 'capacity', 'available', 'reservas_mesa', 'user']
        
