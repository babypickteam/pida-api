from rest_framework import serializers
from .models import GroupPurchaseOrder, GroupPurchaseEvent, GroupPurchaseDiscountRate


class GroupPurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupPurchaseOrder
        fields = (
            'id',
            'event', 'quantity', 'order_time', \
              'status',
        )
        read_only_fields = (
            'order_time', \
              'status',
        )

    def save(self, **kwargs):
        instance = super().save(**kwargs)
        if not instance.is_valid():
            raise serializers.ValidationError()


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
            'orders', 'discount_rates',
            'product', 'closing_time',
        )
