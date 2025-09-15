from random import random
from django.shortcuts import render
from .models import Product
import random


def product_list(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def product_info(request, pk):
    product = Product.objects.get(pk=pk)
    other_products = Product.objects.exclude(pk=product.pk)
    similar_products = random.sample(list(other_products), min(4, other_products.count()))
    return render(request, 'info.html', {'product': product, 'similar_products': similar_products})
