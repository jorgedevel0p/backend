from rest_framework import serializers
from apps.users.models import User
from apps.reservas.models import Reserva

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id','status','date','time', 'date_reserva','mesa']


class UserSerializer(serializers.ModelSerializer):
    reservas_usuario = ReservaSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id','username','reservas_usuario','name','last_name','email', 'type']
        # fields = ['name', 'last_name', '...']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            name=validated_data['name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


    def update(self, instance, validated_data):
        instance.username = validated_data['username']
        instance.name = validated_data['name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.type = validated_data['type']
        instance.set_password(validated_data['password'])
        instance.save()

        return instance