from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductsSerializer


class ProductsView(APIView):
    permission_classes = ()

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            products = Product.objects.all()
            serializer = ProductsSerializer(products, many=True)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    permission_classes = ()

    def get(self, request, id):
        products = Product.objects.filter(id=id).first()
        serializer = ProductsSerializer(products)
        return Response(serializer.data)

    def put(self, request, id):
        product = Product.objects.filter(id=id).first()
        serializer = ProductsSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        product = Product.objects.filter(id=id).first()
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
