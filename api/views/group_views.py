from rest_framework.response import Response
from ..serializers import *
from ..models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status


@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def create_group(request): 
    if request.method == 'POST':
        data = request.data

        serializer = GroupSerializer(data=data)
        if serializer.is_valid(raise_exception=True): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    