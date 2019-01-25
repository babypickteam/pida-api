from django.db import models

from django.conf import settings

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = (
        (0, 'Woman'),
        (1, 'Man'),
    )
    AGE_CHOICES = (
        (0, '~ 19'),
        (1, '20 ~ 26'),
        (2, '27 ~ 36'),
        (3, '36 ~ 50'),
        (4, '51 ~'),
    )
    SKIN_TYPE_CHOICES = (
        (0, 'dry'),
        (1, 'normal'),
        (2, 'oily'),
        (3, 'combination'),
    )

    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES)
    age = models.PositiveSmallIntegerField(choices=AGE_CHOICES)
    skin_type = models.PositiveSmallIntegerField(choices=SKIN_TYPE_CHOICES)
    skin_concerns = models.ManyToManyField('SkinConcern',
                                           blank=True,
                                           related_name='+')
    allergies = models.ManyToManyField('Allergy',
                                       blank=True,
                                       related_name='+')
    default_payment_information = models.OneToOneField('PaymentInformation',
                                                       blank=True,
                                                       null=True,
                                                       on_delete=models.PROTECT,
                                                       related_name='+')
    default_delivery_information = models.OneToOneField('DeliveryInformation',
                                                        blank=True,
                                                        null=True,
                                                        on_delete=models.PROTECT,
                                                        related_name='+')


class SkinConcern(models.Model):
    name = models.CharField(max_length=20)


class Allergy(models.Model):
    name = models.CharField(max_length=20)


class PaymentInformation(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='+')
    issuer = models.CharField(max_length=20)
    card_number = models.CharField(max_length=19)
    expiration_date = models.CharField(max_length=5)
    cvc = models.CharField(max_length=3)
    password_hashed = models.CharField(max_length=255)


class DeliveryInformation(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='+')
    name = models.CharField(max_length=20)
    contact = models.CharField(max_length=15)
    postal_code = models.CharField(max_length=5)
    address_line_road = models.CharField(max_length=40)
    address_line_detail = models.CharField(max_length=40)
