
from os import stat
from re import I
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from .serializers import UserSerializer, ListUserSerializer, CreateUserSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
# Create your views here.


class UserViewSet(ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        # serializer = UserSerializer(queryset, many=True)
        serializer = ListUserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def create(self, request):
       seriializer = CreateUserSerializer(data=request.data)
       if seriializer.is_valid():
           seriializer.save()
           Response()
        
       return Response({}, status=status.HTTP_400_BAD_REQUEST)
           
    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        user.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer