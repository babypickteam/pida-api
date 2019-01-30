from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('notices/',
         views.NoticeList.as_view(),
         name='notice-list'),
    path('notices/<int:pk>/',
         views.NoticeDetail.as_view(),
         name='notice-detail'),
    path('faqs/',
         views.FaqList.as_view(),
         name='faq-list'),
    path('faqs/<int:pk>/',
         views.FaqDetail.as_view(),
         name='faq-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
