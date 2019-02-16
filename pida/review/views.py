from django.shortcuts import render
from rest_framework import generics

from .models import Review
from .serializers import ReviewSerializer


class ReviewList(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetail(generics.RetrieveUpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
