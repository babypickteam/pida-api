from rest_framework import serializers
from .models import Product, Company, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name', 'price', 'company', 'category', \
              'info_seller', 'info_manufacturer', 'info_country', 'info_url',
        )


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id',
            'products',
            'name',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'products',
            'name', 'big_name',
        )
