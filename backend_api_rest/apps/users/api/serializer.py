from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
    # fields = ['name', 'last_name', '...']

  def create(self, validated_data):
     user = User(
         email=validated_data['email'],
         username=validated_data['username']
     )
     user.set_password(validated_data['password'])
     user.save()
     return user

  """ def update(self, instance, validated_data):
    # encriptar password en el actualizar...
     user = User(
         email=validated_data['email'],
         username=validated_data['username'],
         password=validated_data['password']
     )
     
     user.set_password(validated_data['password'])
     user.save()
     return user """