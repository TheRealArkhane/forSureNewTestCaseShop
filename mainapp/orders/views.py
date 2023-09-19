from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import Cart
from orders.models import Order
from orders.serializers import OrderSerializer


class OrderView(APIView):
    def get(self, request, id):
        orders = Order.objects.filter(user_id=id).all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, id):
        cart = Cart.objects.filter(user_id=id).all()
        if len(cart) == 0:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        order = Order(
            user_id=id,
            order_date=request.data.get("order_date")) #логирование
        order.save(force_insert=True)
        for item in cart:
            order.products.add(item.products)
        order.save()
        cart.delete()
        return Response(status=status.HTTP_201_CREATED)

# Create your views here.
