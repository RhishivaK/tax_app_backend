from django.shortcuts import render
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

@api_view(['GET'])
def GetRegisteredUser(request, *args, **kwargs):
    email = request.GET.get('email', None)
    user = User.objects.filter(email=email)

    if user.exists():
        return JsonResponse({'exists': True})
    
    else:
        return JsonResponse({'exists': False})

@api_view(['POST'])
def UserRegister(request, *args, **kwargs):
    data = {
        'first_name': request.data.get('first_name'),
        'middle_name': request.data.get('middle_name'),
        'last_name': request.data.get('last_name'),
        'email': request.data.get('email'),
        'phone_number': request.data.get('phone_number'),
        'pan_number': request.data.get('pan_number'),
        'password': request.data.get('password'),
        'role': request.data.get('role'),
    }
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response({'message': 'Data provided is not valid! Please re-check!'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def UserLogin(request, *args, **kwargs):
    data = {
        'email': request.data.get('email'),
        'password': request.data.get('password'),
    }

    try:
        user_creds = User.objects.get(email=data['email'])
        user_login = UserSerializer(user_creds).data
        print(user_login, "=========")
    except User.DoesNotExist:
        return Response({'Error': 'Invalid User Details'}, status=status.HTTP_401_UNAUTHORIZED)
    
    if check_password(data['password'], user_creds.password) and user_creds.role == "user":
        user = authenticate(request, **data)
        if user is not None:
            login(request, user)
            return Response(user_login, status=status.HTTP_200_OK)
    
    return Response({'Error': 'Login Failed! Please check the credentials and try again!'}, status=status.HTTP_400_BAD_REQUEST)