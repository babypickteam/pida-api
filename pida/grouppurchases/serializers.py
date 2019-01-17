from rest_framework import serializers
from .models import GroupPurchaseOrder, GroupPurchaseEvent, GroupPurchaseDiscountRate


class GroupPurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupPurchaseOrder
        fields = (
            'id',
            'owner', 'event', 'quantity', 'order_time',
            'status',
        )

class _GroupPurchaseDiscountRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupPurchaseDiscountRate
        fields = (
            'quantity', 'rate',
        )

class GroupPurchaseEventSerializer(serializers.ModelSerializer):
    discount_rates = _GroupPurchaseDiscountRateSerializer(many=True, read_only=True)

    class Meta:
        model = GroupPurchaseEvent
        fields = (
            'id',
            'product', 'closing_time', 'orders', 'discount_rates',
        )


