from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from apps.proveedores.models import Proveedor
from apps.proveedores.api.serializer import ProveedorSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated, ))
def proveedor_api_view(request):
  
  # list resources
  if request.method == 'GET':
    proveedores = Proveedor.objects.all()
    proveedores_serializer = ProveedorSerializer(proveedores, many = True) 
    # (many = True) ---> List of proveedores, it expects only 1 object
    return Response(proveedores_serializer.data, status.HTTP_200_OK)

  # create resource
  if request.method == 'POST':
    proveedor_serializer = ProveedorSerializer(data = request.data) # get json and compare to model
    if(proveedor_serializer.is_valid()):
      proveedor_serializer.save()
      return Response({'message': 'Proveedor has been created successfully!'}, status = status.HTTP_200_OK)
    
    return Response(proveedor_serializer.errors, status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def proveedor_detail_api_view(request, pk=None):

  proveedor = Proveedor.objects.filter(id = pk).first()

  if proveedor is None:
    return Response({'message': 'Proveedor not found'}, status = status.HTTP_400_BAD_REQUEST)
  
  # get resource
  if request.method == 'GET':
    proveedor_serializer = ProveedorSerializer(proveedor)
    return Response(proveedor_serializer.data, status.HTTP_200_OK)

  # update resource
  if request.method == 'PUT':
    proveedor_serializer = ProveedorSerializer(proveedor, data = request.data)
    if proveedor_serializer.is_valid():
      proveedor_serializer.save()
      return Response(proveedor_serializer.data, status.HTTP_200_OK)
    
    return Response(proveedor_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

  # delete resource
  if request.method == 'DELETE':
    proveedor.delete() 
    return Response({'message': 'Proveedor has been deleted successfully!'}, status = status.HTTP_200_OK)
  
  
    