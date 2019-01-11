from django.db import models

from django.contrib.auth.models import User
from products.models import Product, Category


class TesterOrder(models.Model):
    STATUS_CHOICES = (
        (1, 'Preparing'),
        (2, 'Shipping'),
        (3, 'Delivered'),
    )

    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='tester_orders')
    category = models.ForeignKey(Category,
                                 on_delete=models.PROTECT,
                                 related_name='+')
    products = models.ManyToManyField(Product,
                                      related_name='+')
    order_time = models.DateTimeField(auto_now_add=True)
    price = models.PositiveIntegerField()
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES,
                                              default=STATUS_CHOICES[0][0])

    def is_valid(self):
        if self.status not in [c[0] for c in self.STATUS_CHOICES]:
            return False
        if self.products.count() != 3:
            return False
        if any(p.category!=self.category for p in self.products.all()):
            return False
        return True