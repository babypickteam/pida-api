from django.db import models
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
                                          related_name='+')
    allergies = models.ManyToManyField('Allergy',
                                       related_name='+')


class SkinConcern(models.Model):
    name = models.TextField(max_length=20)


class Allergy(models.Model):
    name = models.TextField(max_length=20)
