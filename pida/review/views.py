from django.shortcuts import render
from rest_framework import generics

from common.permissions import IsAuthenticatedOwnerOrReadOnly
from .models import Review
from .serializers import ReviewSerializer


class ReviewList(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOwnerOrReadOnly,)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)


class ReviewDetail(generics.RetrieveUpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOwnerOrReadOnly,)
