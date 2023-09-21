from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from categories.models import Category
from categories.serializers import CategorySerializer
from products.serializers import ProductsSerializer


class CategoriesView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, category_id):
        categories = Category.objects.filter(id=category_id).first().get_descendants()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class CategoriesDetails(APIView):
    permission_classes = [AllowAny]
    def get(self, request, category_id):
        category_products = Category.objects.filter(id=category_id).first().products
        serializer = ProductsSerializer(category_products, many=True)
        return Response(serializer.data)
