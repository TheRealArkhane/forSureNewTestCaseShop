from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import Cart
from cart.serializers import CartSerializer


class CartView(APIView):
    permission_classes = ()

    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        cart = Cart.objects.all()
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)


class CartDetail(APIView):
    def get(self, request, id):
        cart = Cart.objects.filter(user_id=id).values()
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)

    def delete(self, request, id):
        carts = Cart.objects.filter(user_id=id).first()
        carts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartSingleEntity(APIView):
    def get(self, request, id, product_in_cart_id):
        product = Cart.objects.filter(id=product_in_cart_id, user_id=id).first()
        serializer = CartSerializer(product)
        return Response(serializer.data)

    def put(self, request, id, product_in_cart_id):
        product = Cart.objects.filter(id=product_in_cart_id, user_id=id).first()
        serializer = CartSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, product_in_cart_id):
        product = Cart.objects.filter(id=product_in_cart_id, user_id=id).first()
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
