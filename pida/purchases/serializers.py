from rest_framework import serializers
from .models import PurchaseOrder, PurchaseItem


class _PurchaseOrderSimpleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = (
            'url',
            'order_time',
        )


class _PurchaseItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PurchaseItem
        fields = (
            'product', 'quantity',
        )


class PurchaseOrderSerializer(serializers.HyperlinkedModelSerializer):
    items = _PurchaseItemSerializer(many=True, read_only=False)

    class Meta:
        model = PurchaseOrder
        fields = (
            'url', 'id',
            'items',
            'owner', 'order_time', 'price', \
              'status', 'payment_information', 'delivery_information',
        )
        read_only_fields = (
            'owner', 'order_time', 'price', \
              'status',
        )
        extra_kwargs = {
            'owner': {'lookup_field': 'username'},
        }

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        instance = PurchaseOrder.objects.create(**validated_data)
        for d in items_data:
            PurchaseItem.objects.create(order=instance, **d)
        return instance

    def save(self, **kwargs):
        instance = super().save(**kwargs)
        if not instance.is_valid():
            instance.items.all().delete()
            instance.delete()
            raise serializers.ValidationError()
