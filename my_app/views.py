
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet, ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from .serializers import UserSerializer, ListUserSerializer, CreateUserSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny
# Create your views here.
from rest_framework.decorators import action
from django.contrib.auth.hashers import make_password

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
    # serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateUserSerializer

        elif self.action == 'list':
            return ListUserSerializer
        else:
            return UserSerializer

    # def get_permissions(self):
    #     if self.action == 'list':
    #         permission_classes = [AllowAny]
    #     else:
    #         permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]



    def perform_create(self, serializer):
        if ('password' in self.request.data):
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()

    @action(detail=False)
    def recent_users(self, request):
        recent_users = User.objects.all().order_by('-date_joined')[:3]
        page = self.paginate_queryset(recent_users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["post", "delete", "put"], permission_classes= [])
    def foo():
        pass




# class UserReadOnlyModelViewSet(ReadOnlyModelViewSet):
#     """
#     """

#     queryset = User.objects.all()
#     serializer_class = UserSerializer
