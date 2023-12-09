from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from service.models import Service
from products.models import Product


class ServiceListView(ListView):
    """Список всех услуг"""
    model = Service
    template_name = 'service/services.html'


class ServiceDetailView(DetailView):
    """Детальный просмотр"""
    template_name = 'service/service.html'
    model = Service
    context_object_name = 'service'

    def get_object(self, queryset=None):
        return get_object_or_404(Service, slug=self.kwargs['service_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ServiceDetailView, self).get_context_data(**kwargs)
        service = self.object
        context['products'] = Product.objects.filter(service=service)
        return context
