from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import Cart
from cart.serializers import CartSerializer
from products.models import Product


class CartDetail(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Получение списка всех товаров в корзине",
        responses={
            200: CartSerializer(many=True),
            500: "Серверная ошибка"},
    )
    def get(self, request):
        cart = Cart.objects.filter(user_id=request.user.id).values()
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Добавление товара в корзину",
        request_body=CartSerializer,
        responses={
            201: CartSerializer,
            400: "Неправильный ввод данных",
            500: "Серверная ошибка",
        },
    )
    def post(self, request):
        price = Product.objects.filter(id=request.data.get("products")).first().price
        cart = Cart(
            products_id=request.data.get("products"),
            quantity=request.data.get("quantity"),
            user_id=request.user.id)
        cart.price = price
        cart.sum = price * cart.quantity
        if cart.quantity == 0:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # I made unique constraint instead of this block

        # -------->

        # if len(Cart.objects.all()) == 0:
        #     cart.save()
        #     return Response(status=status.HTTP_201_CREATED)
        # elif Cart.objects.filter(products_id=request.data.get("products")).first() is None:
        #     cart.save()
        #     return Response(status=status.HTTP_201_CREATED)
        # elif (
        #     Cart.objects.filter(products_id=request.data.get("products")).first().products_id
        #         != request.data.get("products")
        #         or id != Cart.objects.filter(user_id=id).first().user_id):
        #     cart.save()
        #     return Response(status=status.HTTP_201_CREATED)
        # else:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)

        cart.save()
        return Response(status=status.HTTP_201_CREATED)


class CartSingleEntity(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Получение информации о конкретном товаре",
        responses={
            200: CartSerializer,
            500: "Серверная ошибка"},
    )
    def get(self, request, product_in_cart_id):
        product = Cart.objects.filter(id=product_in_cart_id, user_id=request.user.id).first()
        serializer = CartSerializer(product)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Изменение конкретного товара в корзине",
        responses={
            200: CartSerializer(many=True),
            400: "Неправильный ввод данных",
            500: "Серверная ошибка",
        },
        request_body=CartSerializer
    )
    def put(self, request, product_in_cart_id):
        product = Cart.objects.filter(id=product_in_cart_id, user_id=request.user.id).first()
        if product.quantity <= 1:
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = CartSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Удаление конкретного товара в корзине",
        responses={
            204: CartSerializer(many=True),
            500: "Серверная ошибка"
        }
    )
    def delete(self, request, product_in_cart_id):
        product = Cart.objects.filter(id=product_in_cart_id, user_id=request.user.id).first()
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
