from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('users/<str:username>/',
         views.UserDetail.as_view(),
         name='user-detail'),
    path('payment-informations/<int:pk>/',
         views.PaymentInformationDetail.as_view(),
         name='payment-information-detail'),
    path('delivery-informations/<int:pk>/',
         views.DeliveryInformationDetail.as_view(),
         name='delivery-information-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
