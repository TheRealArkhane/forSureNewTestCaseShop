from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from categories.models import Category
from .models import Product
from .serializers import ProductsSerializer


class ProductsView(APIView):

    @swagger_auto_schema(
        operation_summary="Получение списка всех товаров",
        responses={
            200: ProductsSerializer(many=True),
            500: "Серверная ошибка"},
    )
    @permission_classes(AllowAny)
    def get(self, request):
        min_value = request.data.get("min_value")
        max_value = request.data.get("max_value")
        if min_value is None and max_value is None:
            products = Product.objects.all().order_by('id').values()
            serializer = ProductsSerializer(products, many=True)
            return Response(serializer.data)
        elif min_value is not None and max_value is not None:
            products = Product.objects.filter(price__range=(min_value, max_value)).order_by('price').values()
            serializer = ProductsSerializer(products, many=True)
            return Response(serializer.data)
        elif max_value is None:
            products = Product.objects.filter(price__range=(min_value, 1000000000)).order_by('price').values()
            serializer = ProductsSerializer(products, many=True)
            return Response(serializer.data)
        else:
            products = Product.objects.filter(price__range=(0, max_value)).order_by('price').values()
            serializer = ProductsSerializer(products, many=True)
            return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Добавление товаров",
        request_body=ProductsSerializer,
        responses={
            201: ProductsSerializer,
            400: "Неправильный ввод данных",
            500: "Серверная ошибка",
        },
    )
    @permission_classes(IsAdminUser)
    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            product_id = Product.objects.filter(
                name=request.data.get("name"),
                description=request.data.get("description"),
                price=request.data.get("price")
            ).first().id
            Category.objects.filter(id=1).first().products.add(product_id)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):

    @swagger_auto_schema(
        operation_summary="Получение конкретного товара",
        responses={
            200: ProductsSerializer(many=True),
            500: "Серверная ошибка"},
    )
    @permission_classes(AllowAny)
    def get(self, request, id):
        products = Product.objects.filter(id=id).first()
        serializer = ProductsSerializer(products)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Изменение конкретного товара",
        responses={
            202: "Изменения приняты",
            400: "Неправильный ввод данных",
            500: "Серверная ошибка",
        },
        request_body=ProductsSerializer
    )
    @permission_classes(IsAdminUser)
    def put(self, request, id):
        product = Product.objects.filter(id=id).first()
        serializer = ProductsSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Удаление конкретного товара",
        responses={
            204: ProductsSerializer(many=True),
            500: "Серверная ошибка"
        }
    )
    @permission_classes(IsAdminUser)
    def delete(self, request, id):
        product = Product.objects.filter(id=id).first()
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
