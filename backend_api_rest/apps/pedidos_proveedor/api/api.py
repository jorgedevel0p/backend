from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from apps.pedidos_proveedor.models import PedidoProveedor
from apps.pedidos_proveedor.api.serializer import PedidoProveedorSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated, ))
def pedido_proveedor_api_view(request):
  
  # list resources
  if request.method == 'GET':
    pedidos_proveedor = PedidoProveedor.objects.all()
    pedidos_proveedor_serializer = PedidoProveedorSerializer(pedidos_proveedor, many = True) 
    # (many = True) ---> List of pedidos_proveedor, it expects only 1 object
    return Response(pedidos_proveedor_serializer.data, status.HTTP_200_OK)

  # create resource
  if request.method == 'POST':
    pedido_proveedor_serializer = PedidoProveedorSerializer(data = request.data) # get json and compare to model
    if(pedido_proveedor_serializer.is_valid()):
      pedido_proveedor_serializer.save()
      return Response({'message': 'Pedido Proveedor has been created successfully!'}, status = status.HTTP_200_OK)
    
    return Response(pedido_proveedor_serializer.errors, status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def pedido_proveedor_detail_api_view(request, pk=None):

  pedido_proveedor = PedidoProveedor.objects.filter(id = pk).first()

  if pedido_proveedor is None:
    return Response({'message': 'Pedido Proveedor not found'}, status = status.HTTP_400_BAD_REQUEST)
  
  # get resource
  if request.method == 'GET':
    pedido_proveedor_serializer = PedidoProveedorSerializer(pedido_proveedor)
    return Response(pedido_proveedor_serializer.data, status.HTTP_200_OK)

  # update resource
  if request.method == 'PUT':
    pedido_proveedor_serializer = PedidoProveedorSerializer(pedido_proveedor, data = request.data)
    if pedido_proveedor_serializer.is_valid():
      pedido_proveedor_serializer.save()
      return Response(pedido_proveedor_serializer.data, status.HTTP_200_OK)
    
    return Response(pedido_proveedor_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

  # delete resource
  if request.method == 'DELETE':
    pedido_proveedor.delete() 
    return Response({'message': 'Pedido Proveedor has been deleted successfully!'}, status = status.HTTP_200_OK)
  
  
    