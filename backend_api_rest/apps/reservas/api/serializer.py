from apps.reservas.models import Reserva
from rest_framework import serializers
from apps.users.models import User

class ReservaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reserva
        fields = ['id', 'mesa', 'user','status','date','time']