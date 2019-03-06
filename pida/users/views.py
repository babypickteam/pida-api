from django.shortcuts import render
from rest_framework import generics

from common.permissions import IsAuthenticatedOwner
from .models import User, PaymentInformation, DeliveryInformation
from .permissions import IsSelf
from .serializers import UserSerializer, PaymentInformationSerializer, DeliveryInformationSerializer


class UserList(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSelf,)
    lookup_field = 'username'


class PaymentInformationDetail(generics.RetrieveUpdateAPIView):
    queryset = PaymentInformation.objects.all()
    serializer_class = PaymentInformationSerializer
    permission_classes = (IsAuthenticatedOwner,)

    def perform_update(self, serializer):
        instance = self.get_object()
        fields = ['issuer', 'card_number', 'expiration_date',  'cvc', 'password_hashed']
        valid = True
        for f in fields:
            if f in self.request.data:
                value = self.request.data.get(f)
            else:
                value = getattr(instance, f)
            valid = valid and value!=''
        serializer.save(valid=valid)


class DeliveryInformationDetail(generics.RetrieveUpdateAPIView):
    queryset = DeliveryInformation.objects.all()
    serializer_class = DeliveryInformationSerializer
    permission_classes = (IsAuthenticatedOwner,)

    def perform_update(self, serializer):
        instance = self.get_object()
        fields = ['name', 'contact', 'postal_code', 'address_line_road', 'address_line_detail']
        valid = True
        for f in fields:
            if f in self.request.data:
                value = self.request.data.get(f)
            else:
                value = getattr(instance, f)
            valid = valid and value!=''
        serializer.save(valid=valid)
