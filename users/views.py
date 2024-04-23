from rest_framework import viewsets, generics


from utils import response

from users.serializers import UserCreateSerializer, UserUpdateSerializer, UserSerializer
from users.models import User

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    page_size_query_param = 'limit'

class UserViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.success('user created', serializer.data)

        return response.bad_request(serializer.errors)

    def update(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return response.not_found('user not found')
        serializer = UserUpdateSerializer(data=request.data, instance=user)
        if serializer.is_valid():
            return response.success('user updated', serializer.data)

        return response.bad_request(serializer.errors)

    def retrieve(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return response.not_found('user not found')
        serializer = UserSerializer(instance=user)
        return response.success('', serializer.data)

