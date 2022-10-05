from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from apps.cajas.models import Caja
from apps.cajas.api.serializer import CajaSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated, ))
def caja_api_view(request):
  
  # list resources
  if request.method == 'GET':
    cajas = Caja.objects.all()
    cajas_serializer = CajaSerializer(cajas, many = True) 
    # (many = True) ---> List of cajas, it expects only 1 object
    return Response(cajas_serializer.data, status.HTTP_200_OK)

  # create resource
  if request.method == 'POST':
    caja_serializer = CajaSerializer(data = request.data) # get json and compare to model
    if(caja_serializer.is_valid()):
      caja_serializer.save()
      return Response({'message': 'Caja has been created successfully!'}, status = status.HTTP_200_OK)
    
    return Response(caja_serializer.errors, status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def caja_detail_api_view(request, pk=None):

  caja = Caja.objects.filter(id = pk).first()

  if caja is None:
    return Response({'message': 'Caja not found'}, status = status.HTTP_400_BAD_REQUEST)
  
  # get resource
  if request.method == 'GET':
    caja_serializer = CajaSerializer(caja)
    return Response(caja_serializer.data, status.HTTP_200_OK)

  # update resource
  if request.method == 'PUT':
    caja_serializer = MesaSerializer(caja, data = request.data)
    if caja_serializer.is_valid():
      caja_serializer.save()
      return Response(caja_serializer.data, status.HTTP_200_OK)
    
    return Response(caja_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

  # delete resource
  if request.method == 'DELETE':
    caja.delete() 
    return Response({'message': 'Mesa has been deleted successfully!'}, status = status.HTTP_200_OK)
  
  
    