from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from news.models import News


class NewsListView(ListView):
    """Список всех новостей"""
    model = News
    template_name = 'news/news.html'


class NewsDetailView(DetailView):
    """Детальный просмотр"""
    template_name = 'news/news_detail.html'
    model = News
    context_object_name = 'news'

    def get_object(self, queryset=None):
        return get_object_or_404(News, slug=self.kwargs['news_slug'])
