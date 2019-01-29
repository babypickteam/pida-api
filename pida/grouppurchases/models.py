from django.db import models
from django.conf import settings

from users.models import PaymentInformation, DeliveryInformation
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
    event = models.ForeignKey('GroupPurchaseEvent',
                              on_delete=models.PROTECT,
                              related_name='orders')
    quantity = models.PositiveSmallIntegerField()
    order_time = models.DateTimeField(auto_now_add=True)
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
               and self.quantity > 0

    def __str__(self):
        return ' '.join([super().__str__(), str(self.order_time)])


class GroupPurchaseEvent(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.PROTECT,
                                related_name='+')
    closing_time = models.DateTimeField()

    def __str__(self):
        return ' '.join([super().__str__(), str(self.product), str(self.closing_time)])


class GroupPurchaseDiscountRate(models.Model):
    event = models.ForeignKey(GroupPurchaseEvent,
                              on_delete=models.CASCADE,
                              related_name='discount_rates')
    quantity = models.PositiveSmallIntegerField()
    rate = models.FloatField()

    def __str__(self):
        return ' '.join([super().__str__(), str(self.quantity), str(self.rate)])
