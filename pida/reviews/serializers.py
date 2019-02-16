from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = (
            'url', 'id',
            'owner', 'product', 'content', 'written_time'
        )
        read_only_fields = (
            'owner',
        )
        extra_kwargs = {
            'owner': {'lookup_field': 'username'},
        }
