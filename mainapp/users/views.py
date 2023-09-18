from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UsersSerializer


class UsersView(APIView):
    permission_classes = ()

    def get(self, request):
        users = User.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    permission_classes = ()

    def get(self, request, id):
        user = User.objects.filter(id=id).first()
        serializer = UsersSerializer(user)
        return Response(serializer.data)

    def put(self, request, id):
        user = User.objects.filter(id=id).first()
        serializer = UsersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        user = User.objects.filter(id=id).first()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
