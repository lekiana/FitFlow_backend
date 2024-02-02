from rest_framework.response import Response
from ..serializers import *
from ..models import *
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(["GET"])
def get_company_budgets(request):
    company_id = request.query_params.get('company_id')

    data = Budget.objects.filter(company=company_id)
    serializer = BudgetSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST", "GET"])
def add_budget(request): 
    if request.method == 'POST':
        data = request.data

        serializer = BudgetSerializer(data=data)
        if serializer.is_valid(raise_exception=True): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    