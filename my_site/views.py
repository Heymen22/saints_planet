from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader

from .models import Product, Catalog


# Create your views here.


def index(request):
    template = loader.get_template('my_site/index.html')
    bestsellers = Product.objects.order_by('sold')

    tShirts = Product.objects.filter(catalog__name__startswith='Рубашки')

    shoes = Product.objects.filter(catalog__name__startswith='Обувь')

    context = {
        'bestsellers': bestsellers,
        'tShirts': tShirts,
        'shoes': shoes,
    }
    return HttpResponse(template.render(request=request, context=context))


def catalog(request, catalog=None):
    template = loader.get_template('my_site/catalog.html')
    context = {'categories': Catalog.objects.all()}
    if catalog:
        context['current_category'] = get_object_or_404(Catalog, pk=catalog)

        if context['current_category']:
            context['products'] = context['current_category'].product_set.all()

    return HttpResponse(template.render(request=request, context=context))


def product_detail(request, product):
    template = loader.get_template('my_site/product.html')
    context = {'product': get_object_or_404(Product, pk=product)}
    return HttpResponse(template.render(request=request, context=context))
