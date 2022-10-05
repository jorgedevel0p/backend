from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from apps.detalle_ordenes.models import DetalleOrden
from apps.detalle_ordenes.api.serializer import DetalleOrdenSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated, ))
def detalle_orden_api_view(request):
  
  # list resources
  if request.method == 'GET':
    detalle_ordenes = DetalleOrden.objects.all()
    detalle_ordenes_serializer = DetalleOrdenSerializer(detalle_ordenes, many = True) 
    # (many = True) ---> List of detalle_ordenes, it expects only 1 object
    return Response(detalle_ordenes_serializer.data, status.HTTP_200_OK)

  # create resource
  if request.method == 'POST':
    detalle_orden_serializer = DetalleOrdenSerializer(data = request.data) # get json and compare to model
    if(detalle_orden_serializer.is_valid()):
      detalle_orden_serializer.save()
      return Response({'message': 'Detalle Orden has been created successfully!'}, status = status.HTTP_200_OK)
    
    return Response(detalle_orden_serializer.errors, status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def detalle_orden_detail_api_view(request, pk=None):

  detalle_orden = DetalleOrden.objects.filter(id = pk).first()

  if detalle_orden is None:
    return Response({'message': 'Detalle Orden not found'}, status = status.HTTP_400_BAD_REQUEST)
  
  # get resource
  if request.method == 'GET':
    detalle_orden_serializer = DetalleOrdenSerializer(detalle_orden)
    return Response(detalle_orden_serializer.data, status.HTTP_200_OK)

  # update resource
  if request.method == 'PUT':
    detalle_orden_serializer = DetalleOrdenSerializer(detalle_orden, data = request.data)
    if detalle_orden_serializer.is_valid():
      detalle_orden_serializer.save()
      return Response(detalle_orden_serializer.data, status.HTTP_200_OK)
    
    return Response(detalle_orden_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

  # delete resource
  if request.method == 'DELETE':
    detalle_orden.delete() 
    return Response({'message': 'Detalle Orden has been deleted successfully!'}, status = status.HTTP_200_OK)
  
  
    