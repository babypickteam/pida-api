from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('reviews/',
         views.ReviewList.as_view(),
         name='review-list'),
    path('reviews/<int:pk>/',
         views.ReviewDetail.as_view(),
         name='review-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)