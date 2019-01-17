from django.db import models

from django.conf import settings

from products.models import Product


class PurchaseOrder(models.Model):
    STATUS_CHOICES = (
        (1, 'Preparing'),
        (2, 'Shipping'),
        (3, 'Delivered'),
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='purchase_orders')
    order_time = models.DateTimeField(auto_now_add=True)
    price = models.PositiveIntegerField()
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES,
                                              default=STATUS_CHOICES[0][0])

    def is_valid(self):
        return self.status in [c[0] for c in self.STATUS_CHOICES] \
               and self.items.count() > 0 \
               and self.price == sum(i.product.price*i.quantity for i in self.items.all()) \
               and all(i.quantity>0 for i in self.items.all())


class PurchaseItem(models.Model):
    order = models.ForeignKey('PurchaseOrder',
                              on_delete=models.CASCADE,
                              related_name='items')
    product = models.ForeignKey(Product,
                                on_delete=models.PROTECT,
                                related_name='+')
    quantity = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = (('order', 'product'),)
