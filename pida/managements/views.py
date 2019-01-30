from django.shortcuts import render
from rest_framework import generics

from .models import Notice, Faq
from .serializers import NoticeSerializer, FaqSerializer


class NoticeList(generics.ListAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer


class NoticeDetail(generics.RetrieveAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer


class FaqList(generics.ListAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer


class FaqDetail(generics.RetrieveAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
