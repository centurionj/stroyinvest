from django.views.generic import TemplateView

from products.models import Product
from service.models import Service
from vacancies.models import Vacancies

class RobotsTxtView(TemplateView):
    template_name = 'seo/robots.txt'
    content_type = 'text/plain'


class SitemapView(TemplateView):
    template_name = 'seo/sitemap.xml'
    content_type = 'application/xml'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        context['services'] = Service.objects.all()
        context['vacancies'] = Vacancies.objects.all()
        return context
