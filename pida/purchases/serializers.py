from rest_framework import serializers
from .models import PurchaseOrder, PurchaseItem


class _PurchaseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseItem
        fields = (
            'product', 'quantity',
        )


class PurchaseOrderSerializer(serializers.ModelSerializer):
    items = _PurchaseItemSerializer(many=True, read_only=False)

    class Meta:
        model = PurchaseOrder
        fields = (
            'id',
            'items',
            'owner', 'order_time', 'price', \
              'status',
        )

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        instance = PurchaseOrder.objects.create(**validated_data)
        for d in items_data:
            PurchaseItem.objects.create(order=instance, **d)
        return instance
