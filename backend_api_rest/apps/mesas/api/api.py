from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from apps.mesas.models import Mesa
from apps.mesas.api.serializer import MesaSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated, ))
def mesa_api_view(request):
  
  # list resources
  if request.method == 'GET':
    mesas = Mesa.objects.all()
    mesas_serializer = MesaSerializer(mesas, many = True) 
    # (many = True) ---> List of mesas, it expects only 1 object
    return Response(mesas_serializer.data, status.HTTP_200_OK)

  # create resource
  if request.method == 'POST':
    mesa_serializer = MesaSerializer(data = request.data) # get json and compare to model
    if(mesa_serializer.is_valid()):
      mesa_serializer.save()
      return Response({'message': 'Mesa has been created successfully!'}, status = status.HTTP_200_OK)
    
    return Response(mesa_serializer.errors, status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def mesa_detail_api_view(request, pk=None):

  mesa = Mesa.objects.filter(id = pk).first()

  if mesa is None:
    return Response({'message': 'Mesa not found'}, status = status.HTTP_400_BAD_REQUEST)
  
  # get resource
  if request.method == 'GET':
    mesa_serializer = MesaSerializer(mesa)
    return Response(mesa_serializer.data, status.HTTP_200_OK)

  # update resource
  if request.method == 'PUT':
    mesa_serializer = MesaSerializer(mesa, data = request.data)
    if mesa_serializer.is_valid():
      mesa_serializer.save()
      return Response(mesa_serializer.data, status.HTTP_200_OK)
    
    return Response(mesa_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

  # delete resource
  if request.method == 'DELETE':
    mesa.delete() 
    return Response({'message': 'Mesa has been deleted successfully!'}, status = status.HTTP_200_OK)
  
  
    