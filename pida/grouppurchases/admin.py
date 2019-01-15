from django.contrib import admin

from .models import GroupPurchaseOrder, GroupPurchaseEvent, GroupPurchaseDiscountRate


admin.site.register(GroupPurchaseOrder)
admin.site.register(GroupPurchaseEvent)
admin.site.register(GroupPurchaseDiscountRate)
