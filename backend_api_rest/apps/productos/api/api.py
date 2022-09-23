from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from apps.productos.models import Producto
from apps.productos.api.serializer import ProductoSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated, ))
def producto_api_view(request):

    # list resources
    if request.method == 'GET':
        productos = Producto.objects.all()
        # (many = True) ---> List of productos, it expects only 1 object
        productos_serializer = ProductoSerializer(productos, many=True)
        return Response(productos_serializer.data, status.HTTP_200_OK)

    # create resource
    if request.method == 'POST':
        producto_serializer = ProductoSerializer(
            data=request.data)  # get json and compare to model
        if (producto_serializer.is_valid()):
            producto_serializer.save()
            return Response({'message': 'Producto has been created successfully!'}, status=status.HTTP_200_OK)

        return Response(producto_serializer.errors, status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def producto_detail_api_view(request, pk=None):

    producto = Producto.objects.filter(id=pk).first()

    if producto is None:
        return Response({'message': 'Producto not found'}, status=status.HTTP_400_BAD_REQUEST)

    # get resource
    if request.method == 'GET':
        producto_serializer = ProductoSerializer(producto)
        return Response(producto_serializer.data, status.HTTP_200_OK)

    # update resource
    if request.method == 'PUT':
        producto_serializer = ProductoSerializer(producto, data=request.data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return Response(producto_serializer.data, status.HTTP_200_OK)

        return Response(producto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete resource
    if request.method == 'DELETE':
        producto.delete()
        return Response({'message': 'Producto has been deleted successfully!'}, status=status.HTTP_200_OK)
