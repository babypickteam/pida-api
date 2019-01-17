from django.shortcuts import render
from rest_framework import generics

from common.permissions import IsAuthenticatedOwner
from .models import TesterOrder
from .serializers import TesterOrderSerializer


class TesterOrderList(generics.CreateAPIView):
    queryset = TesterOrder.objects.all()
    serializer_class = TesterOrderSerializer
    permission_classes = (IsAuthenticatedOwner,)

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


class TesterOrderDetail(generics.RetrieveAPIView):
    queryset = TesterOrder.objects.all()
    serializer_class = TesterOrderSerializer
    permission_classes = (IsAuthenticatedOwner,)
