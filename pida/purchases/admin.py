from django.contrib import admin

from .models import PurchaseOrder, PurchaseItem


admin.site.register(PurchaseOrder)
admin.site.register(PurchaseItem)
