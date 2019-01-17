from django.shortcuts import render
from rest_framework import generics

from common.permissions import IsAuthenticatedOwnerOrReadOnly
from .models import GroupPurchaseOrder, GroupPurchaseEvent
from .serializers import GroupPurchaseOrderSerializer, GroupPurchaseEventSerializer


class GroupPurchaseOrderList(generics.CreateAPIView):
    queryset = GroupPurchaseOrder.objects.all()
    serializer_class = GroupPurchaseOrderSerializer
    permission_classes = (IsAuthenticatedOwnerOrReadOnly,)

    def perform_create(self, serializer):
        user = self.request.user
        payment_information = user.default_payment_information
        payment_information.pk = None
        payment_information.save()
        delivery_information = user.default_delivery_information
        delivery_information.pk = None
        delivery_information.save()
        serializer.save(owner=user,
                        payment_information=payment_information,
                        delivery_information=delivery_information)


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
