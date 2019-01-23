from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('users/',
         views.UserList.as_view(),
         name='user-list'),
    path('users/<str:username>/',
         views.UserDetail.as_view(),
         name='user-detail'),
    path('payment-informations/<int:pk>/',
         views.PaymentInformationDetail.as_view(),
         name='paymentinformation-detail'),
    path('delivery-informations/<int:pk>/',
         views.DeliveryInformationDetail.as_view(),
         name='deliveryinformation-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
