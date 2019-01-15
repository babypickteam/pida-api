from django.contrib import admin

from .models import Product, Company, Category, BigCategory


admin.site.register(Product)
admin.site.register(Company)
admin.site.register(Category)
admin.site.register(BigCategory)
