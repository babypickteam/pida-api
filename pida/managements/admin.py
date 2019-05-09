from django.contrib import admin

from .models import Notice, Faq, Agreement


admin.site.register(Notice)
admin.site.register(Faq)
admin.site.register(Agreement)
