from django.db import models

from django.contrib.auth.models import User


class Product(models.Model):
    name = models.TextField(max_length=60)
    price = models.PositiveIntegerField()
    company = models.ForeignKey('Company',
                                on_delete=models.PROTECT,
                                related_name='products')
    category = models.ForeignKey('Category',
                                 on_delete=models.PROTECT,
                                 related_name='products')
    info_seller = models.TextField(max_length=100)
    info_manufacturer = models.TextField(max_length=100)
    info_country = models.TextField(max_length=40)
    info_url = models.TextField(max_length=200)


class Company(models.Model):
    name = models.TextField(max_length=40)


class Category(models.Model):
    name = models.TextField(max_length=20)
    big_category = models.ForeignKey('BigCategory',
                                     on_delete=models.PROTECT,
                                     related_name='subcategories')


class BigCategory(models.Model):
    name = models.TextField(max_length=20)