from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from apps.users.models import User
from apps.users.api.serializer import UserSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, ))
def user_api_view(request):
  
  # list resources
  if request.method == 'GET':
    users = User.objects.all()
    users_serializer = UserSerializer(users, many = True) # (many = True) ---> List of users, it expects only 1 object
    return Response(users_serializer.data, status.HTTP_200_OK)

  # create resource
  if request.method == 'POST':
    user_serializer = UserSerializer(data = request.data) # get json and compare to model
    if(user_serializer.is_valid()):
      user_serializer.save()
      return Response({'message': 'User has been created successfully!'}, status = status.HTTP_200_OK)
    
    return Response(user_serializer.errors, status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk=None):

  user = User.objects.filter(id = pk).first()

  if user is None:
    return Response({'message': 'User not found'}, status = status.HTTP_400_BAD_REQUEST)
  
  # get resource
  if request.method == 'GET':
    user_serializer = UserSerializer(user)
    return Response(user_serializer.data, status.HTTP_200_OK)

  # update resource
  if request.method == 'PUT':
    user_serializer = UserSerializer(user, data = request.data)
    if user_serializer.is_valid():
      user_serializer.save()
      return Response(user_serializer.data, status.HTTP_200_OK)
    
    return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

  # delete resource
  if request.method == 'DELETE':
    user.delete() 
    return Response({'message': 'User has been deleted successfully!'}, status = status.HTTP_200_OK)
  
  
    