from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from apps.boletas.models import Boleta
from apps.boletas.api.serializer import BoletaSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated, ))
def boleta_api_view(request):
  
  # list resources
  if request.method == 'GET':
    boletas = Boleta.objects.all()
    boletas_serializer = BoletaSerializer(boletas, many = True) 
    # (many = True) ---> List of boletas, it expects only 1 object
    return Response(boletas_serializer.data, status.HTTP_200_OK)

  # create resource
  if request.method == 'POST':
    boleta_serializer = BoletaSerializer(data = request.data) # get json and compare to model
    if(boleta_serializer.is_valid()):
      boleta_serializer.save()
      return Response({'message': 'Boleta has been created successfully!'}, status = status.HTTP_200_OK)
    
    return Response(boleta_serializer.errors, status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def boleta_detail_api_view(request, pk=None):

  boleta = Boleta.objects.filter(id = pk).first()

  if boleta is None:
    return Response({'message': 'Boleta not found'}, status = status.HTTP_400_BAD_REQUEST)
  
  # get resource
  if request.method == 'GET':
    boleta_serializer = BoletaSerializer(boleta)
    return Response(boleta_serializer.data, status.HTTP_200_OK)

  # update resource
  if request.method == 'PUT':
    boleta_serializer = BoletaSerializer(boleta, data = request.data)
    if boleta_serializer.is_valid():
      boleta_serializer.save()
      return Response(boleta_serializer.data, status.HTTP_200_OK)
    
    return Response(boleta_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

  # delete resource
  if request.method == 'DELETE':
    boleta.delete() 
    return Response({'message': 'Boleta has been deleted successfully!'}, status = status.HTTP_200_OK)
  
  
    