from django.shortcuts import render
from rest_framework import generics

from common.permissions import IsAuthenticatedOwner
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer


class PurchaseOrderList(generics.CreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = (IsAuthenticatedOwner,)

    def perform_create(self, serializer):
        user = self.request.user
        price = sum(i['product'].price*i['quantity'] for i in serializer.validated_data['items'])
        payment_information = user.default_payment_information
        payment_information.pk = None
        payment_information.save()
        delivery_information = user.default_delivery_information
        delivery_information.pk = None
        delivery_information.save()
        serializer.save(owner=user,
                        price=price,
                        payment_information=payment_information,
                        delivery_information=delivery_information)


class PurchaseOrderDetail(generics.RetrieveAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = (IsAuthenticatedOwner,)
