from rest_framework.serializers import ModelSerializer

from .models import User


class UsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'birthday',
            'password'
        ]

