from rest_framework import serializers
from .models import TesterOrder


class TesterOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TesterOrder
        fields = (
            'id',
            'category', 'products', 'order_time', \
              'price', 'status',
        )
        read_only_fields = (
            'order_time', \
            'price', 'status',
        )

    def save(self, **kwargs):
        instance = super().save(**kwargs)
        if not instance.is_valid():
            raise serializers.ValidationError()
