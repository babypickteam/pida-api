from django.shortcuts import render
from rest_framework import generics

from .models import TesterOrder
from .serializers import TesterOrderSerializer


class TesterOrderList(generics.CreateAPIView):
    queryset = TesterOrder.objects.all()
    serializer_class = TesterOrderSerializer


class TesterOrderDetail(generics.RetrieveAPIView):
    queryset = TesterOrder.objects.all()
    serializer_class = TesterOrderSerializer
