from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import Cart
from orders.models import Order
from orders.serializers import OrderSerializer


class OrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user_id=request.user.id).all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        cart = Cart.objects.filter(user_id=request.user.id).all()
        if len(cart) == 0:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        order = Order(
            user_id=request.user.id
            )
        order.save(force_insert=True)
        for item in cart:
            order.products.add(item.products)
        order.save()
        cart.delete()
        return Response(status=status.HTTP_201_CREATED)

