from curses.ascii import US
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class ListUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)

class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'username', 'email',)