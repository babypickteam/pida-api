from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import Notice, Faq, Agreement
from .serializers import NoticeSerializer, FaqSerializer, AgreementSerializer


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


class AgreementList(generics.ListAPIView):
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer


class AgreementDetail(generics.RetrieveAPIView):
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer
