from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from apps.platos.models import Plato
from apps.platos.api.serializer import PlatoSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated, ))
def plato_api_view(request):
  
  # list resources
  if request.method == 'GET':
    platos = Plato.objects.all()
    platos_serializer = PlatoSerializer(platos, many = True) 
    # (many = True) ---> List of platos, it expects only 1 object
    return Response(platos_serializer.data, status.HTTP_200_OK)

  # create resource
  if request.method == 'POST':
    plato_serializer = PlatoSerializer(data = request.data) # get json and compare to model
    if(plato_serializer.is_valid()):
      plato_serializer.save()
      return Response({'message': 'Plato has been created successfully!'}, status = status.HTTP_200_OK)
    
    return Response(plato_serializer.errors, status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def plato_detail_api_view(request, pk=None):

  plato = Plato.objects.filter(id = pk).first()

  if plato is None:
    return Response({'message': 'Plato not found'}, status = status.HTTP_400_BAD_REQUEST)
  
  # get resource
  if request.method == 'GET':
    plato_serializer = PlatoSerializer(plato)
    return Response(plato_serializer.data, status.HTTP_200_OK)

  # update resource
  if request.method == 'PUT':
    plato_serializer = PlatoSerializer(plato, data = request.data)
    if plato_serializer.is_valid():
      plato_serializer.save()
      return Response(plato_serializer.data, status.HTTP_200_OK)
    
    return Response(plato_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

  # delete resource
  if request.method == 'DELETE':
    plato.delete() 
    return Response({'message': 'Plato has been deleted successfully!'}, status = status.HTTP_200_OK)
  
  
    