from rest_framework import serializers
from .models import Notice, Faq


class NoticeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notice
        fields = (
            'url', 'id',
            'title', 'content', 'written_time'
        )


class FaqSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faq
        fields = (
            'url', 'id',
            'title', 'content', 'written_time'
        )
