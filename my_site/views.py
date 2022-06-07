from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Product


# Create your views here.


def index(request):
    template = loader.get_template('my_site/index.html')
    bestsellers = Product.objects.order_by('solded')
    for product in bestsellers:
        product.price_with_discount = product.price * (100 - product.discount) / 100

    context = {
        'bestsellers': bestsellers,
    }
    return HttpResponse(template.render(request=request, context=context))
