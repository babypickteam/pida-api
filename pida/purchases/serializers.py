from rest_framework import serializers
from .models import PurchaseOrder, PurchaseItem


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = (
            'id',
            'owner', 'items', 'order_time', 'price',
            'status',
        )


class PurchaseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseItem
        fields = (
            'id',
            'product', 'number',
        )
