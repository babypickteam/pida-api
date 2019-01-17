from rest_framework import serializers
from .models import Product, Company, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name', 'price', 'company', 'category',
            'info_seller', 'info_manufacturer', 'info_country', 'info_url',
        )


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id',
            'name', 'products',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name', 'big_name', 'products'
        )
