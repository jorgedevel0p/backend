from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from apps.reservas.models import Reserva
from apps.reservas.api.serializer import ReservaSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated, ))
def reserva_api_view(request):
  
  # list resources
  if request.method == 'GET':
    reservas = Reserva.objects.all()
    reservas_serializer = ReservaSerializer(reservas, many = True) 
    # (many = True) ---> List of reservas, it expects only 1 object
    return Response(reservas_serializer.data, status.HTTP_200_OK)

  # create resource
  if request.method == 'POST':
    reserva_serializer = ReservaSerializer(data = request.data) # get json and compare to model
    if(reserva_serializer.is_valid()):
      reserva_serializer.save()
      return Response({'message': 'Reserva has been created successfully!'}, status = status.HTTP_200_OK)
    
    return Response(reserva_serializer.errors, status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def reserva_detail_api_view(request, pk=None):

  reserva = Reserva.objects.filter(id = pk).first()

  if reserva is None:
    return Response({'message': 'Reserva not found'}, status = status.HTTP_400_BAD_REQUEST)
  
  # get resource
  if request.method == 'GET':
    reserva_serializer = ReservaSerializer(reserva)
    return Response(reserva_serializer.data, status.HTTP_200_OK)

  # update resource
  if request.method == 'PUT':
    reserva_serializer = ReservaSerializer(reserva, data = request.data)
    if reserva_serializer.is_valid():
      reserva_serializer.save()
      return Response(reserva_serializer.data, status.HTTP_200_OK)
    
    return Response(reserva_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

  # delete resource
  if request.method == 'DELETE':
    reserva.delete() 
    return Response({'message': 'Reserva has been deleted successfully!'}, status = status.HTTP_200_OK)
  
  
    