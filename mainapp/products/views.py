from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductsSerializer


class ProductsView(APIView):
    permission_classes = ()

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
            products = Product.objects.filter(price__range=(min_value, 1000000000000)).order_by('price').values()
            serializer = ProductsSerializer(products, many=True)
            return Response(serializer.data)
        else:
            products = Product.objects.filter(price__range=(0, max_value)).order_by('price').values()
            serializer = ProductsSerializer(products, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
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
