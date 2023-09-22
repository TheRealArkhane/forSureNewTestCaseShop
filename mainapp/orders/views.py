from dadata import Dadata
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import Cart
from orders.models import Order
from orders.serializers import OrderSerializer

token = "ced0414f954e7d1cd4d83c73d0abdfaa6aeaeff2"
secret = "eab02a24c999f149deba9ba4e23baec57473a6c1"
dadata = Dadata(token, secret)


class OrderView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Получение списка всех заказов пользователя",
        responses={
            200: OrderSerializer(many=True),
            500: "Серверная ошибка"},
    )
    def get(self, request):
        orders = Order.objects.filter(user_id=request.user.id).all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Оформление заказа",
        request_body=OrderSerializer,
        responses={
            201: OrderSerializer,
            400: "Неправильный ввод данных",
            500: "Серверная ошибка",
        },
    )
    def post(self, request):
        cart = Cart.objects.filter(user_id=request.user.id).all()
        if len(cart) == 0:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        order = Order(
            user_id=request.user.id,
            address=request.data.get("address"),
        )
        order.address = dadata.clean(name="address", source=order.address)
        order.address = order.address['result']
        order.save(force_insert=True)
        sum = 0
        total_quantity = 0
        for item in cart:
            order.products.add(item.products)
            total_quantity += item.quantity
            sum += item.sum
        order.total_quantity = total_quantity
        order.sum = sum
        order.save()
        cart.delete()
        return Response(status=status.HTTP_201_CREATED)
