from django.db import models
from django.conf import settings

from users.models import PaymentInformation, DeliveryInformation
from products.models import Product, Category


class TesterOrder(models.Model):
    STATUS_CHOICES = (
        (1, 'Preparing'),
        (2, 'Shipping'),
        (3, 'Delivered'),
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
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
    payment_information = models.ForeignKey(PaymentInformation,
                                            on_delete=models.PROTECT,
                                            related_name='+')
    delivery_information = models.ForeignKey(DeliveryInformation,
                                             on_delete=models.PROTECT,
                                             related_name='+')

    def is_valid(self):
        return self.status in [c[0] for c in self.STATUS_CHOICES] \
               and self.payment_information.valid \
               and self.delivery_information.valid \
               and self.products.count() == 2 \
               and all(p.category==self.category for p in self.products.all())

    def __str__(self):
        return ' '.join([super().__str__(), str(self.order_time)])
