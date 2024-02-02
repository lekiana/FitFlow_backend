from rest_framework.response import Response
from ..serializers import *
from ..models import *
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import timedelta, date


@api_view(['DELETE'])
def delete_standing_order(request):
    pk = request.query_params.get('pk')
    standing_order = StandingOrder.objects.get(pk=pk)
    standing_order.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(["POST", "GET"])
def add_standind_order(request): 
    if request.method == 'POST':
        data = request.data

        serializer = StandingOrderSerializer(data=data)
        if serializer.is_valid(raise_exception=True): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE', "PATCH"])
def update_standing_order(request):
    pk = request.query_params.get('pk')
    standing_order = StandingOrder.objects.get(pk=pk)
    interval = standing_order.interval
    standing_order.due_date += timedelta(days=interval)
    standing_order.save()
    return Response(status=status.HTTP_200_OK)
    
@api_view(["GET"])
def get_standing_orders(request): 
    data = request.data
    company_id = request.query_params.get('company_id')

    data = StandingOrder.objects.filter(means__company=company_id)
    serializer = StandingOrderSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(["GET"])
def get_standing_orders_sum(request):
    company_id = request.query_params.get('company_id')

    data = StandingOrder.objects.filter(means__company=company_id).filter(due_date__lte=date.today())
    serializer = StandingOrderSerializer(data, many=True)

    sum = 0
    for transaction in serializer.data:
        sum += transaction['value']   

    return Response(sum, status=status.HTTP_200_OK)

