from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('group-purchase-orders/',
         views.GroupPurchaseOrderList.as_view(),
         name='grouppurchaseorder-list'),
    path('group-purchase-orders/<int:pk>/',
         views.GroupPurchaseOrderDetail.as_view(),
         name='grouppurchaseorder-detail'),
    path('group-purchase-events/',
         views.GroupPurchaseEventList.as_view(),
         name='grouppurchaseevent-list'),
    path('group-purchase-events/<int:pk>/',
         views.GroupPurchaseEventDetail.as_view(),
         name='grouppurchaseevent-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
