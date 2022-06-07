from django.core.management import BaseCommand, CommandError
from my_site.models import *
from . import _test_data
from random import randint


class Command(BaseCommand):
    help = 'Fills database with test data'

    def handle(self, *args, **kwargs):
        Catalog.objects.all().delete()
        self.stdout.write('old catalogs deleted')
        Product.objects.all().delete()
        self.stdout.write('old products deleted')
        ProductImage.objects.all().delete()
        self.stdout.write('old product images deleted')

        Catalog.objects.bulk_create([Catalog(name=catalog_data['name']) for catalog_data in _test_data.Catalogs])
        self.stdout.write('Catalogs created')
        Product.objects.bulk_create([Product(catalog_id=_test_data.Catalogs.index(product_data['catalog']) + 1,
                                             name=product_data['name'], sex=product_data['sex'],
                                             stock=product_data['stock'],
                                             description=product_data['description'], price=product_data['price'],
                                             discount=product_data['discount'], solded=randint(0, 1000)) for
                                     product_data
                                     in _test_data.Products])
        self.stdout.write('Products created')
        ProductImage.objects.bulk_create([ProductImage(
            product_id=_test_data.Products.index(product_images_data['product']) + 1,
            image=product_images_data['image']) for product_images_data in _test_data.ProductImages])
        self.stdout.write('ProductImages created')
