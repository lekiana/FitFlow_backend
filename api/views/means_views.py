from rest_framework.response import Response
from ..serializers import *
from ..models import *
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(["GET"])
def get_company_means(request):
    company_id = request.query_params.get('company_id')

    data = Means.objects.filter(company=company_id)
    serializer = MeansSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET", "POST"])
def add_account(request):
    if request.method == 'POST':
        data = request.data

        serializer = MeansSerializer(data=data)
        if serializer.is_valid(raise_exception=True): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    