from django.db import models

from django.conf import settings

from products.models import Product


class Review(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='reviews')
    product = models.ForeignKey(Product,
                                on_delete=models.PROTECT,
                                related_name='reviews')
    content = models.TextField()
    written_time = models.DateTimeField(auto_now_add=True)
