from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from vacancies.models import Vacancies


class VacanciesListView(ListView):
    """Список всех новостей"""
    model = Vacancies
    template_name = 'vacancies/vacancies.html'


class VacancyDetailView(DetailView):
    """Детальный просмотр"""
    template_name = 'vacancies/vacancy_detail.html'
    model = Vacancies
    context_object_name = 'vacancy'

    def get_object(self, queryset=None):
        return get_object_or_404(Vacancies, slug=self.kwargs['vacancy_slug'])
