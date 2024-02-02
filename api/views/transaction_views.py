from rest_framework.response import Response
from ..serializers import *
from ..models import *
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(["DELETE"])
def delete_transaction(request):
    pk = request.query_params.get('pk')
    transaction = Transaction.objects.get(pk=pk)
    transaction.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(["POST", "GET"])
def add_transaction(request): 
    if request.method == 'POST':
        data = request.data

        serializer = TransactionSerializer(data=data)
        if serializer.is_valid(raise_exception=True): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
def get_company_transactions(request): 
    data = request.data
    company_id = request.query_params.get('company_id')

    data = Transaction.objects.filter(means__company=company_id)
    serializer = TransactionSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(["GET"])
def get_category_transactions(request):
    category_id = request.query_params.get('category_id')
    end_date = request.query_params.get('end_date')
    start_date = request.query_params.get('start_date')

    data = Transaction.objects.filter(category=category_id).filter(date__range=(start_date, end_date))
    serializer = TransactionSerializer(data, context={'request': request}, many=True)

    sum = 0
    for transaction in serializer.data:
        sum += transaction['value']

    return Response(sum, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_sum(request):
    company_id = request.query_params.get('company_id')
    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')

    revenue = Transaction.objects.filter(category__company=company_id).filter(category__type=1).filter(date__range=(start_date, end_date))
    expense = Transaction.objects.filter(category__company=company_id).filter(category__type=2).filter(date__range=(start_date, end_date))

    revenue_serializer = TransactionSerializer(revenue, context={'request': request}, many=True)
    expense_serializer = TransactionSerializer(expense, context={'request': request}, many=True)

    revenue_sum = 0
    for transaction in revenue_serializer.data:
        revenue_sum += transaction['value']

    expense_sum = 0
    for transaction in expense_serializer.data:
        expense_sum += transaction['value']    

    sum = revenue_sum - expense_sum

    return Response({'sum': sum, 'revenue': revenue_sum, 'expense': expense_sum}, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_available_means(request):
    company_id = request.query_params.get('company_id')

    revenue = Transaction.objects.filter(category__company=company_id).filter(category__type=1)
    expense = Transaction.objects.filter(category__company=company_id).filter(category__type=2)

    revenue_serializer = TransactionSerializer(revenue, context={'request': request}, many=True)
    expense_serializer = TransactionSerializer(expense, context={'request': request}, many=True)

    revenue_sum = 0
    for transaction in revenue_serializer.data:
        revenue_sum += transaction['value']

    expense_sum = 0
    for transaction in expense_serializer.data:
        expense_sum += transaction['value']    

    sum = revenue_sum - expense_sum

    return Response(sum, status=status.HTTP_200_OK)


