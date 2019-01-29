from rest_framework import serializers
from .models import Product, Brand, Category, Ingredient


class _IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = (
            'name', 'ewg_grade',
        )


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    ingredients = _IngredientSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = (
            'url', 'id',
            'name', 'capacity', 'price', 'brand', 'category', \
              'info_seller', 'info_manufacturer', 'info_country', 'info_url', \
              'image', 'ingredients',
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
