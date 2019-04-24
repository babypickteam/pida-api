from rest_framework import serializers
from .models import Notice, Faq, Agreement


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


class AgreementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agreement
        fields = (
            'url', 'id',
            'title', 'content', 'written_time', 'visible'
        )
