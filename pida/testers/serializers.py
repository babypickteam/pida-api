from rest_framework import serializers
from .models import TesterOrder


class _TesterOrderSimpleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TesterOrder
        fields = (
            'url',
            'order_time',
        )


class TesterOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TesterOrder
        fields = (
            'url', 'id',
            'owner', 'category', 'products', 'order_time', \
              'price', 'status', 'payment_information', 'delivery_information',
        )
        read_only_fields = (
            'owner', 'order_time', \
            'price', 'status',
        )
        extra_kwargs = {
            'owner': {'lookup_field': 'username'},
        }

    def save(self, **kwargs):
        instance = super().save(**kwargs)
        if not instance.is_valid():
            instance.delete()
            raise serializers.ValidationError()
