from django.db import models as django_models
from django.urls import reverse
from mptt import models as mptt_models


# Create your models here.
class Catalog(mptt_models.MPTTModel):
    name = django_models.CharField(max_length=1024)
    parent = mptt_models.TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=django_models.CASCADE)

    class MPTTMeta:
        order_insertions_by = ['name']

    def __str__(self):
        return f'Категория {self.name}'

    def get_absolute_url(self):
        return reverse('catalog_by_category', args=[self.id])


class Product(django_models.Model):
    class Sex(django_models.TextChoices):
        MEN = ('M', 'Для мужчин')
        WOMEN = ('W', 'Для женщин')
        UNISEX = ('U', 'Унисекс')
        NONE = ('N', 'Не указано')

    catalog = django_models.ForeignKey(Catalog, on_delete=django_models.CASCADE)
    name = django_models.CharField(max_length=1024)
    stock = django_models.PositiveIntegerField()
    description = django_models.TextField()
    price = django_models.DecimalField(max_digits=10, decimal_places=2)
    discount = django_models.IntegerField()
    sex = django_models.CharField(max_length=1, choices=Sex.choices)
    sold = django_models.PositiveIntegerField()

    def price_with_discount(self):
        return self.price * (100 - self.discount) / 100

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('product', args=[self.id])


class ProductImage(django_models.Model):
    product = django_models.ForeignKey(Product, on_delete=django_models.CASCADE)
    image = django_models.ImageField()

    def __str__(self):
        return f'{self.image.name}'


class Characteristic(django_models.Model):
    name = django_models.CharField(max_length=1024)
    catalog = django_models.ForeignKey(Catalog, on_delete=django_models.CASCADE)

    def __str__(self):
        return f'Характеристика {self.name}'


class CharacteristicValue(django_models.Model):
    characteristic = django_models.ForeignKey(Characteristic, on_delete=django_models.CASCADE)
    value = django_models.CharField(max_length=1024)

    def __str__(self):
        return f'Значение {self.value} - {self.characteristic}'
