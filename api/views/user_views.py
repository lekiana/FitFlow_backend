from rest_framework.response import Response
from ..serializers import *
from ..models import *
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

@api_view(['DELETE'])
def delete_user(request):
    pk = request.query_params.get('pk')
    user = User.objects.get(pk=pk)
    user.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(["POST", "GET"])
def create_user(request): 
    if request.method == 'POST':
        data = request.data

        try:
            if not validate_password(data.get('password')):
                try:
                    user = User.objects.create_user(username=data.get('username'), 
                                                    password=data.get('password'), 
                                                    first_name=data.get('first_name'), 
                                                    last_name=data.get('last_name'),
                                                    email=data.get('email'),
                                                    )
                    user.save()
                    groups = [data.get('groups')]
                    user.groups.set(groups)
                    return Response(status=status.HTTP_201_CREATED) 
                except:
                    return Response({'error_msg': 'This username is taken. Try another one.'},  status=status.HTTP_400_BAD_REQUEST)      
        
        except Exception as e:
            return Response({'error_msg': e},  status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_company_users(request): 
    data = request.data
    company_id = request.query_params.get('company_id')

    data = User.objects.filter(groups__company=company_id)
    serializer = UserSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def authenticate_user(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        user_data = get_user_data(user)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': user_data}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials', 'username': username, 'password': password},  status=status.HTTP_400_BAD_REQUEST)


def get_user_data(user):
    user_groups = user.groups.all()
    group_ids = [group.id for group in user_groups]
    company = Company.objects.get(group=group_ids[0])
    company_serializer = CompanySerializer(company)
    company_data = company_serializer.data

    user_data = {
    'id': user.id,
    'username': user.username,
    "first_name": user.first_name,
    "last_name": user.last_name,
    'email': user.email,
    'company_data': company_data,
    }

    return user_data