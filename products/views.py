from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404

from products.models import Product


class ProductList(generic.ListView):
    # model = Product
    queryset = Product.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetail(generic.DetailView):
    # model = get_object_or_404(Product, id='pk')
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'


