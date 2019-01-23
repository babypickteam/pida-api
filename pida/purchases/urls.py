from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('purchase-orders/',
         views.PurchaseOrderList.as_view(),
         name='purchaseorder-list'),
    path('purchase-orders/<int:pk>/',
         views.PurchaseOrderDetail.as_view(),
         name='purchaseorder-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
