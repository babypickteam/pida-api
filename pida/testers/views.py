from django.shortcuts import render
from rest_framework import generics

from common.permissions import IsAuthenticatedOwner
from .models import TesterOrder
from .serializers import TesterOrderSerializer


class TesterOrderList(generics.CreateAPIView):
    queryset = TesterOrder.objects.all()
    serializer_class = TesterOrderSerializer
    permission_classes = (IsAuthenticatedOwner,)


class TesterOrderDetail(generics.RetrieveAPIView):
    queryset = TesterOrder.objects.all()
    serializer_class = TesterOrderSerializer
    permission_classes = (IsAuthenticatedOwner,)
