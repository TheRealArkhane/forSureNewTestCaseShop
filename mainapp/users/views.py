from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UsersSerializer


class UsersView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        operation_summary="Получение списка всех пользователей",
        responses={
            200: UsersSerializer(many=True),
            500: "Серверная ошибка"},
    )
    def get(self, request):
        users = User.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Добавление пользователей",
        request_body=UsersSerializer,
        responses={
            201: UsersSerializer,
            400: "Неправильный ввод данных",
            500: "Серверная ошибка",
        },
    )
    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Получение конкретного пользователя",
        responses={
            200: UsersSerializer(many=True),
            500: "Серверная ошибка"},
    )
    def get(self, request):
        user = User.objects.filter(id=request.user.id).first()
        serializer = UsersSerializer(user)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Изменение данных пользователя",
        responses={
            202: "Изменения приняты",
            400: "Неправильный ввод данных",
            500: "Серверная ошибка",
        },
        request_body=UsersSerializer
    )
    def put(self, request):
        user = User.objects.filter(id=request.user.id).first()
        serializer = UsersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Удаление конкретного товара",
        responses={
            204: UsersSerializer(many=True),
            500: "Серверная ошибка"
        }
    )
    def delete(self, request):
        user = User.objects.filter(id=request.user.id).first()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
