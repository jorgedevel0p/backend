from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from apps.detalle_pedidos.models import DetallePedido
from apps.detalle_pedidos.api.serializer import DetallePedidoSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated, ))
def detalle_pedido_api_view(request):
  
  # list resources
  if request.method == 'GET':
    detalle_pedidos = DetallePedido.objects.all()
    detalle_pedidos_serializer = DetallePedidoSerializer(detalle_pedidos, many = True) 
    # (many = True) ---> List of detalle_pedidos, it expects only 1 object
    return Response(detalle_pedidos_serializer.data, status.HTTP_200_OK)

  # create resource
  if request.method == 'POST':
    detalle_pedido_serializer = DetallePedidoSerializer(data = request.data) # get json and compare to model
    if(detalle_pedido_serializer.is_valid()):
      detalle_pedido_serializer.save()
      return Response({'message': 'Detalle Pedido has been created successfully!'}, status = status.HTTP_200_OK)
    
    return Response(detalle_pedido_serializer.errors, status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def detalle_pedido_detail_api_view(request, pk=None):

  detalle_pedido = DetallePedido.objects.filter(id = pk).first()

  if detalle_pedido is None:
    return Response({'message': 'Detalle Pedido not found'}, status = status.HTTP_400_BAD_REQUEST)
  
  # get resource
  if request.method == 'GET':
    detalle_pedido_serializer = DetallePedidoSerializer(detalle_pedido)
    return Response(detalle_pedido_serializer.data, status.HTTP_200_OK)

  # update resource
  if request.method == 'PUT':
    detalle_pedido_serializer = DetallePedidoSerializer(detalle_pedido, data = request.data)
    if detalle_pedido_serializer.is_valid():
      detalle_pedido_serializer.save()
      return Response(detalle_pedido_serializer.data, status.HTTP_200_OK)
    
    return Response(detalle_pedido_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

  # delete resource
  if request.method == 'DELETE':
    detalle_pedido.delete() 
    return Response({'message': 'Detalle Pedido has been deleted successfully!'}, status = status.HTTP_200_OK)
  
  
    