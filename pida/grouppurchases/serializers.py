from rest_framework import serializers
from .models import GroupPurchaseOrder, GroupPurchaseEvent, GroupPurchaseDiscountRate


class GroupPurchaseOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroupPurchaseOrder
        fields = (
            'url', 'id',
            'owner', 'event', 'quantity', 'order_time', \
              'status', 'payment_information', 'delivery_information',
        )
        read_only_fields = (
            'owner', 'order_time', \
              'status',
        )
        extra_kwargs = {
            'owner': {'lookup_field': 'username'},
        }

    def save(self, **kwargs):
        instance = super().save(**kwargs)
        if not instance.is_valid():
            instance.delete()
            raise serializers.ValidationError()


class _GroupPurchaseDiscountRateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroupPurchaseDiscountRate
        fields = (
            'quantity', 'rate',
        )


class GroupPurchaseEventSerializer(serializers.HyperlinkedModelSerializer):
    discount_rates = _GroupPurchaseDiscountRateSerializer(many=True, read_only=True)

    class Meta:
        model = GroupPurchaseEvent
        fields = (
            'url', 'id',
            'orders', 'discount_rates',
            'product', 'closing_time',
        )
