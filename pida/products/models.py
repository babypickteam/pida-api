from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=60)
    capacity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    brand = models.ForeignKey('Brand',
                              on_delete=models.PROTECT,
                              related_name='products')
    category = models.ForeignKey('Category',
                                 on_delete=models.PROTECT,
                                 related_name='products')
    info_seller = models.CharField(max_length=100)
    info_manufacturer = models.CharField(max_length=100)
    info_country = models.CharField(max_length=40)
    info_url = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return ' '.join([super().__str__(), self.name])


class Brand(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return ' '.join([super().__str__(), self.name])


class Category(models.Model):
    name = models.CharField(max_length=20)
    big_name = models.CharField(max_length=20)

    class Meta:
        unique_together = (('name', 'big_name'),)

    def __str__(self):
        return ' '.join([super().__str__(), self.name, self.big_name])
