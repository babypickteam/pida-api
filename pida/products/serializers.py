from rest_framework import serializers
from .models import Product, Brand, Category


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = (
            'url', 'id',
            'name', 'price', 'brand', 'category', \
              'info_seller', 'info_manufacturer', 'info_country', 'info_url', \
              'image',
        )


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'url', 'id',
            'products',
            'name',
        )


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = (
            'url', 'id',
            'products',
            'name', 'big_name',
        )
