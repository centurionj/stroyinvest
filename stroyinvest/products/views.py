from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from service.models import Service
from products.models import Product


class ProductsListView(ListView):
    """Список всех продуктов"""
    model = Product
    template_name = 'products/products.html'


class ProductsDetailView(DetailView):
    """Детальный просмотр"""
    template_name = 'products/product.html'
    model = Product
    context_object_name = 'product'

    def get_object(self, queryset=None):
        return get_object_or_404(Product, slug=self.kwargs['product_slug'])
