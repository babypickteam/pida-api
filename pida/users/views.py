from django.shortcuts import render
from rest_framework import generics

from .models import PaymentInformation, DeliveryInformation
from .serializers import PaymentInformationSerializer, DeliveryInformationSerializer


class PaymentInformationDetail(generics.RetrieveUpdateAPIView):
    queryset = PaymentInformation.objects.all()
    serializer_class = PaymentInformationSerializer


class DeliveryInformationDetail(generics.RetrieveUpdateAPIView):
    queryset = DeliveryInformation.objects.all()
    serializer_class = DeliveryInformationSerializer
