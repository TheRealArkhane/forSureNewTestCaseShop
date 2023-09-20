from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from categories.models import Category
from categories.serializers import CategorySerializer
from products.serializers import ProductsSerializer


class CategoriesView(APIView):
    def get(self, request, id):
        categories = Category.objects.filter(id=id).first().get_descendants()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class CategoriesDetails(APIView):
    def get(self, request, id):
        category_products = Category.objects.filter(id=id).first().products
        serializer = ProductsSerializer(category_products, many=True)
        return Response(serializer.data)
