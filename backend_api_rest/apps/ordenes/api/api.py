from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from apps.ordenes.models import Orden
from apps.ordenes.api.serializer import OrdenSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated, ))
def orden_api_view(request):

    # list resources
    if request.method == 'GET':
        ordenes = Orden.objects.all()
        # (many = True) ---> List of ordenes, it expects only 1 object
        ordenes_serializer = OrdenSerializer(ordenes, many=True)
        return Response(ordenes_serializer.data, status.HTTP_200_OK)

    # create resource
    if request.method == 'POST':
        orden_serializer = OrdenSerializer(data=request.data)  # get json and compare to model
        if (orden_serializer.is_valid()):
            orden_serializer.save()
            print(orden_serializer.data)
            return Response(orden_serializer.data, status=status.HTTP_200_OK)
        return Response(orden_serializer.errors, status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def orden_detail_api_view(request, pk=None):

    orden = Orden.objects.filter(id=pk).first()

    if orden is None:
        return Response({'message': 'Orden not found'}, status=status.HTTP_400_BAD_REQUEST)

    # get resource
    if request.method == 'GET':
        orden_serializer = OrdenSerializer(orden)
        return Response(orden_serializer.data, status.HTTP_200_OK)

    # update resource
    if request.method == 'PUT':
        orden_serializer = OrdenSerializer(orden, data=request.data)
        if orden_serializer.is_valid():
            orden_serializer.save()
            return Response(orden_serializer.data, status.HTTP_200_OK)

        return Response(orden_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete resource
    if request.method == 'DELETE':
        orden.delete()
        return Response({'message': 'Orden has been deleted successfully!'}, status=status.HTTP_200_OK)
