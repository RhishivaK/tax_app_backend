from django.contrib.auth import authenticate, login, logout

from utils import response

from users.models import User
from users.serializers import UserSerializer

from _auth.serializers import LoginSerializer, SignupSerializer, MeSerializer


from rest_framework import viewsets

class AuthViewSet(viewsets.ViewSet):
    """
    User Login, Logout, Signup View Sets
    """

    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return response.bad_request(serializer.errors)
        data = serializer.data

        user = authenticate(request, email=data['email'], password=data['password'])
        if user == None:
            return response.auth_required('Invalid Credentials')

        login(request, user)
        return response.success('', UserSerializer(user).data)


    def logout(self, request):
        logout(request)
        return response.success('successfully logged out')


    def signup(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.success('user successfully registered', serializer.data)
        
        return response.bad_request(serializer.errors, {})


    def me(self, request):
        user = request.user
        serializer = UserSerializer(instance=request.user, data={
            "first_name": user.first_name,
            "last_name": user.last_name ,
            "email": user.email,
            "phone": user.phone,
            "pan": user.pan,
            "maritial_status": user.maritial_status,
            "reward_points": user.reward_points + 1
        })
        if serializer.is_valid():
            serializer.save()
            return response.success('', serializer.data)
        return response.auth_required('', meta=serializer.errors)

