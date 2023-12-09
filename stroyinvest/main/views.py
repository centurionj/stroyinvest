from django.shortcuts import render
from django.views.generic import TemplateView

from news.models import News
from service.models import Service

class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['services'] = Service.objects.all()
        context['news'] = News.objects.all()
        return context


def contacts(request):
    return render(request, 'main/contacts.html')

def about_us(request):
    return render(request, 'main/about-us.html')