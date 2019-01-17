from django.shortcuts import render
from rest_framework import generics

from common.permissions import IsAuthenticatedOwnerOrReadOnly
from .models import GroupPurchaseOrder, GroupPurchaseEvent
from .serializers import GroupPurchaseOrderSerializer, GroupPurchaseEventSerializer


class GroupPurchaseOrderList(generics.CreateAPIView):
    queryset = GroupPurchaseOrder.objects.all()
    serializer_class = GroupPurchaseOrderSerializer
    permission_classes = (IsAuthenticatedOwnerOrReadOnly,)


class GroupPurchaseOrderDetail(generics.RetrieveAPIView):
    queryset = GroupPurchaseOrder.objects.all()
    serializer_class = GroupPurchaseOrderSerializer
    permission_classes = (IsAuthenticatedOwnerOrReadOnly,)


class GroupPurchaseEventList(generics.ListAPIView):
    queryset = GroupPurchaseEvent.objects.all()
    serializer_class = GroupPurchaseEventSerializer


class GroupPurchaseEventDetail(generics.RetrieveAPIView):
    queryset = GroupPurchaseEvent.objects.all()
    serializer_class = GroupPurchaseEventSerializer
