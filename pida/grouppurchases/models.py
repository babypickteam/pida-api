from django.db import models
from django.conf import settings

from products.models import Product


class GroupPurchaseOrder(models.Model):
    STATUS_CHOICES = (
        (0, 'Ongoing'),
        (1, 'Preparing'),
        (2, 'Shipping'),
        (3, 'Delivered'),
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='group_purchase_orders')
    event = models.ManyToManyField('GroupPurchaseEvent',
                                    related_name='orders')
    quantity = models.PositiveSmallIntegerField()
    order_time = models.DateTimeField(auto_now_add=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES,
                                              default=STATUS_CHOICES[0][0])

    def is_valid(self):
        return self.status in [c[0] for c in self.STATUS_CHOICES] \
               and self.quantity > 0


class GroupPurchaseEvent(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.PROTECT,
                                related_name='+')
    closing_time = models.DateTimeField()


class GroupPurchaseDiscountRate(models.Model):
    event = models.ForeignKey(GroupPurchaseEvent,
                              on_delete=models.CASCADE,
                              related_name='discount_rates')
    quantity = models.PositiveSmallIntegerField()
    rate = models.FloatField()