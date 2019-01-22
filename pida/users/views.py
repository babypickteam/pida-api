from django.shortcuts import render
from rest_framework import generics

from common.permissions import IsAuthenticatedOwner
from .models import User, PaymentInformation, DeliveryInformation
from .permissions import IsSelf
from .serializers import UserSerializer, PaymentInformationSerializer, DeliveryInformationSerializer


class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSelf,)
    lookup_field = 'username'


class PaymentInformationDetail(generics.RetrieveUpdateAPIView):
    queryset = PaymentInformation.objects.all()
    serializer_class = PaymentInformationSerializer
    permission_classes = (IsAuthenticatedOwner,)


class DeliveryInformationDetail(generics.RetrieveUpdateAPIView):
    queryset = DeliveryInformation.objects.all()
    serializer_class = DeliveryInformationSerializer
    permission_classes = (IsAuthenticatedOwner,)
