from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('tester-orders/',
         views.TesterOrderList.as_view(),
         name='tester-order-list'),
    path('tester-orders/<int:pk>/',
         views.TesterOrderDetail.as_view(),
         name='tester-order-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
