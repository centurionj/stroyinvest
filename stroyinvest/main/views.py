from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from service.models import Service
from common.view_mixin import TitleListMixin


class IndexView(TitleListMixin, TemplateView):
    """Клас отображения индексной страницы"""
    template_name = 'main/index.html'
    title = 'Стройинвест - главная'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['services'] = Service.objects.all()
        return context


def contacts(request):
    """Отображение страницы контактов"""
    return render(request, 'main/contacts.html')


def about_us(request):
    """Отображение страницы о нас"""
    return render(request, 'main/about-us.html')


def favicon_view(request):
    favicon_path = 'main/static/main/images/favicon/favicon.ico'

    with open(favicon_path, 'rb') as f:
        favicon_content = f.read()

    return HttpResponse(favicon_content, content_type='image/x-icon')
