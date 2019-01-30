from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('products/',
         views.ProductList.as_view(),
         name='product-list'),
    path('products/<int:pk>/',
         views.ProductDetail.as_view(),
         name='product-detail'),
    path('brands/',
         views.BrandList.as_view(),
         name='brand-list'),
    path('brands/<int:pk>/',
         views.BrandDetail.as_view(),
         name='brand-detail'),
    path('categories/',
         views.CategoryList.as_view(),
         name='category-list'),
    path('categories/<int:pk>/',
         views.CategoryDetail.as_view(),
         name='category-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
