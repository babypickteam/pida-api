from django.shortcuts import render
from rest_framework import generics

from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer


class PurchaseOrderList(generics.CreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class PurchaseOrderDetail(generics.RetrieveAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
