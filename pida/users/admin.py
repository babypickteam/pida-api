from django.contrib import admin

from .models import User, SkinConcern, Allergy, PaymentInformation, DeliveryInformation


admin.site.register(User)
admin.site.register(SkinConcern)
admin.site.register(Allergy)
admin.site.register(PaymentInformation)
admin.site.register(DeliveryInformation)
