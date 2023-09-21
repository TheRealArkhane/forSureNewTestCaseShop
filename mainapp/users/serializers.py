from rest_framework.serializers import ModelSerializer

from .models import User


class UsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'birth_date',
            'is_superuser',
            'is_staff',
            'password'
        ]

