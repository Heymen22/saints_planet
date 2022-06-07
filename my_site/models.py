from django.db import models


# Create your models here.
class Catalog(models.Model):
    name = models.CharField(max_length=1024)

    def __str__(self):
        return f'Категория {self.name}'


class Image(models.Model):
    image = models.ImageField()

    def __str__(self):
        return f'{self.image.name}'


class Product(models.Model):
    class Sex(models.TextChoices):
        MEN = ('M', 'Для мужчин')
        WOMEN = ('W', 'Для женщин')
        UNISEX = ('U', 'Унисекс')
        NONE = ('N', 'Не указано')

    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    product_id = models.IntegerField
    name = models.CharField(max_length=1024)
    stock = models.PositiveIntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField()
    images = models.ManyToManyField(Image)

    def __str__(self):
        return f'{self.name}'


class Characteristic(models.Model):
    name = models.CharField(max_length=1024)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)

    def __str__(self):
        return f'Характеристика {self.name}'


class CharacteristicValue(models.Model):
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE)
    value = models.CharField(max_length=1024)

    def __str__(self):
        return f'Значение {self.value} - {self.characteristic}'
