from rest_framework import serializers
from .models import TesterOrder


class TesterOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TesterOrder
        fields = (
            'id',
            'owner', 'category', 'products', 'order_time',
            'price', 'status',
        )
