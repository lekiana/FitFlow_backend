from rest_framework.response import Response
from ..serializers import *
from ..models import *
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(["GET"])
def get_transactions_categories(request):
    company_id = request.query_params.get('company_id')

    data = TransactionCategory.objects.filter(company=company_id)
    serializer = TransactionCategorySerializer(data, context={'request': request}, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_category(request):
    pk = request.query_params.get('pk')

    data = TransactionCategory.objects.get(pk=pk)
    serializer = TransactionCategorySerializer(data, context={'request': request})

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_type_categories(request):
    company_id = request.query_params.get('company_id')
    transaction_type = request.query_params.get('transaction_type')

    data = TransactionCategory.objects.filter(company=company_id).filter(type=transaction_type)
    serializer = TransactionCategorySerializer(data, context={'request': request}, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST", "GET"])
def add_category(request): 
    if request.method == 'POST':
        data = request.data

        serializer = TransactionCategorySerializer(data=data)
        if serializer.is_valid(raise_exception=True): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    