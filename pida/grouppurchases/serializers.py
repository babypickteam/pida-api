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


class GroupPurchaseEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupPurchaseEvent
        fields = (
            'id',
            'product', 'closing_time', 'orders', 'discount_rates',
        )


class GroupPurchaseDiscountRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupPurchaseDiscountRate
        fields = (
            'id',
            'event', 'quantity', 'rate',
        )
