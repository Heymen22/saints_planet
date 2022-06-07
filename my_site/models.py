from django.db import models


# Create your models here.
class Image(models.Model):
    image_url = models.URLField()


class AbstractProduct(models.Model):
    class Sex(models.Choices):
        MEN = 'M', 'Для мужчин'
        WOMEN = 'W', 'Для женщин'
        UNISEX = 'U', 'Унисекс'
        NONE = 'N', 'Не указано'

    product_id = models.IntegerField
    name = models.CharField(max_length=1024)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField()
    images = models.ManyToManyField(ProductImages)
    sex = models.CharField(max_length=1, choices=Sex.choices, default=Sex.NONE)

    class Meta:
        abstract = True


class Sizes(models.Choices):
    S = 'S', 'S'
    M = 'M', 'M'
    L = 'L', 'L'
    XL = 'XL', 'XL'
    XXL = 'XXL', 'XXL'


class T_shirt(AbstractProduct):
    size = models.CharField(max_length='3', choices=Sizes.choices)
