from rest_framework import serializers
from .models import TesterOrder


class TesterOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TesterOrder
        fields = (
            'id',
            'category', 'products', 'order_time', \
              'price', 'status',
        )
        read_only_fields = (
            'price',
        )

    def save(self, **kwargs):
        instance = super().save(**kwargs)
        if not instance.is_valid():
            raise serializers.ValidationError()
