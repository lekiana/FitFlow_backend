from rest_framework.response import Response
from ..serializers import *
from ..models import *
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(["DELETE"])
def delete_budget_entry(request): 
    pk = request.query_params.get('pk')
    budgetEntry = BudgetEntry.objects.get(pk=pk)
    budgetEntry.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(["GET"])
def get_budget_entries(request): 
    budget_id = request.query_params.get('budget_id')
    transaction_type = request.query_params.get('transaction_type')

    data = BudgetEntry.objects.filter(budget=budget_id).filter(category__type=transaction_type)
    serializer = BudgetEntrySerializer(data, context={'request': request}, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST", "GET"])
def add_budget_entry(request): 
    if request.method == 'POST':
        data = request.data

        serializer = BudgetEntrySerializer(data=data)
        if serializer.is_valid(raise_exception=True): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
def get_planned_profit(request):
    budget_id = request.query_params.get('budget_id')

    revenue = BudgetEntry.objects.filter(budget=budget_id).filter(category__type=1)
    expense = BudgetEntry.objects.filter(budget=budget_id).filter(category__type=2)

    revenue_serializer = BudgetEntrySerializer(revenue, many=True)
    expense_serializer = BudgetEntrySerializer(expense, many=True)

    revenue_sum = 0
    for transaction in revenue_serializer.data:
        revenue_sum += transaction['value']

    expense_sum = 0
    for transaction in expense_serializer.data:
        expense_sum += transaction['value']    

    sum = revenue_sum - expense_sum

    return Response(sum, status=status.HTTP_200_OK)
