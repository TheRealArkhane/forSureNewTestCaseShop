from rest_framework import serializers

from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'products',
            'sum',
            'total_quantity',
            'user_id',
            'address',
            'status',
            'order_date'
        ]
