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

        for item in cart:
            order = Order(
                order_date=request.data.get("order_date"),
                quantity=item.quantity,
                price=item.price,
                user_id=item.user.id
            )
            order.save()
        # cart.delete()
        return Response(status=status.HTTP_201_CREATED)

# Create your views here.
