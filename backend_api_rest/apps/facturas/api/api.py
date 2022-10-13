from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from apps.facturas.models import Factura
from apps.facturas.api.serializer import FacturaSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated, ))
def factura_api_view(request):
  
  # list resources
  if request.method == 'GET':
    facturas = Factura.objects.all()
    facturas_serializer = FacturaSerializer(facturas, many = True) 
    # (many = True) ---> List of facturas, it expects only 1 object
    return Response(facturas_serializer.data, status.HTTP_200_OK)

  # create resource
  if request.method == 'POST':
    factura_serializer = FacturaSerializer(data = request.data) # get json and compare to model
    if(factura_serializer.is_valid()):
      factura_serializer.save()
      return Response({'message': 'Factura has been created successfully!'}, status = status.HTTP_200_OK)
    
    return Response(factura_serializer.errors, status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def factura_detail_api_view(request, pk=None):

  factura = Factura.objects.filter(id = pk).first()

  if factura is None:
    return Response({'message': 'Factura not found'}, status = status.HTTP_400_BAD_REQUEST)
  
  # get resource
  if request.method == 'GET':
    factura_serializer = FacturaSerializer(factura)
    return Response(factura_serializer.data, status.HTTP_200_OK)

  # update resource
  if request.method == 'PUT':
    factura_serializer = FacturaSerializer(factura, data = request.data)
    if factura_serializer.is_valid():
      factura_serializer.save()
      return Response(factura_serializer.data, status.HTTP_200_OK)
    
    return Response(factura_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

  # delete resource
  if request.method == 'DELETE':
    factura.delete() 
    return Response({'message': 'Factura has been deleted successfully!'}, status = status.HTTP_200_OK)
  
  
    