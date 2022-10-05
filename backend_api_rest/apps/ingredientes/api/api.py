from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from apps.ingredientes.models import Ingrediente
from apps.ingredientes.api.serializer import IngredienteSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated, ))
def ingrediente_api_view(request):
  
  # list resources
  if request.method == 'GET':
    ingredientes = Ingrediente.objects.all()
    ingredientes_serializer = IngredienteSerializer(ingredientes, many = True) 
    # (many = True) ---> List of ingredientes, it expects only 1 object
    return Response(ingredientes_serializer.data, status.HTTP_200_OK)

  # create resource
  if request.method == 'POST':
    ingrediente_serializer = IngredienteSerializer(data = request.data) # get json and compare to model
    if(ingrediente_serializer.is_valid()):
      ingrediente_serializer.save()
      return Response({'message': 'Ingrediente has been created successfully!'}, status = status.HTTP_200_OK)
    
    return Response(ingrediente_serializer.errors, status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def ingrediente_detail_api_view(request, pk=None):

  ingrediente = Ingrediente.objects.filter(id = pk).first()

  if ingrediente is None:
    return Response({'message': 'Ingrediente not found'}, status = status.HTTP_400_BAD_REQUEST)
  
  # get resource
  if request.method == 'GET':
    ingrediente_serializer = IngredienteSerializer(ingrediente)
    return Response(ingrediente_serializer.data, status.HTTP_200_OK)

  # update resource
  if request.method == 'PUT':
    ingrediente_serializer = IngredienteSerializer(ingrediente, data = request.data)
    if ingrediente_serializer.is_valid():
      ingrediente_serializer.save()
      return Response(ingrediente_serializer.data, status.HTTP_200_OK)
    
    return Response(ingrediente_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

  # delete resource
  if request.method == 'DELETE':
    ingrediente.delete() 
    return Response({'message': 'Ingrediente has been deleted successfully!'}, status = status.HTTP_200_OK)
  
  
    