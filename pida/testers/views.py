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
        serializer.save(owner=user)


class TesterOrderDetail(generics.RetrieveAPIView):
    queryset = TesterOrder.objects.all()
    serializer_class = TesterOrderSerializer
    permission_classes = (IsAuthenticatedOwner,)
