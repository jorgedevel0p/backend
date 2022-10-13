from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from apps.movimientos_caja.models import MovimientoCaja
from apps.movimientos_caja.api.serializer import MovimientoCajaSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated, ))
def movimiento_caja_api_view(request):
  
  # list resources
  if request.method == 'GET':
    movimientos_caja = MovimientoCaja.objects.all()
    movimientos_caja_serializer = MovimientoCajaSerializer(movimientos_caja, many = True) 
    # (many = True) ---> List of movimientos_caja, it expects only 1 object
    return Response(movimientos_caja_serializer.data, status.HTTP_200_OK)

  # create resource
  if request.method == 'POST':
    movimiento_caja_serializer = MovimientoCajaSerializer(data = request.data) # get json and compare to model
    if(movimiento_caja_serializer.is_valid()):
      movimiento_caja_serializer.save()
      return Response({'message': 'MovimientoCaja has been created successfully!'}, status = status.HTTP_200_OK)
    
    return Response(movimiento_caja_serializer.errors, status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movimiento_caja_detail_api_view(request, pk=None):

  movimiento_caja = MovimientoCaja.objects.filter(id = pk).first()

  if movimiento_caja is None:
    return Response({'message': 'MovimientoCaja not found'}, status = status.HTTP_400_BAD_REQUEST)
  
  # get resource
  if request.method == 'GET':
    movimiento_caja_serializer = MovimientoCajaSerializer(movimiento_caja)
    return Response(movimiento_caja_serializer.data, status.HTTP_200_OK)

  # update resource
  if request.method == 'PUT':
    movimiento_caja_serializer = MovimientoCajaSerializer(movimiento_caja, data = request.data)
    if movimiento_caja_serializer.is_valid():
      movimiento_caja_serializer.save()
      return Response(movimiento_caja_serializer.data, status.HTTP_200_OK)
    
    return Response(movimiento_caja_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

  # delete resource
  if request.method == 'DELETE':
    movimiento_caja.delete() 
    return Response({'message': 'MovimientoCaja has been deleted successfully!'}, status = status.HTTP_200_OK)
  
  
    