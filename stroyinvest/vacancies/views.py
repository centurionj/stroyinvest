from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from vacancies.models import Vacancies
from common.view_mixin import TitleListMixin, TitleDetailMixin


class VacanciesListView(TitleListMixin, ListView):
    """Список всех новостей"""
    model = Vacancies
    template_name = 'vacancies/vacancies.html'
    title = 'Стройинвест - вакансии'


class VacancyDetailView(TitleDetailMixin, DetailView):
    """Детальный просмотр"""
    template_name = 'vacancies/vacancy_detail.html'
    model = Vacancies
    context_object_name = 'vacancy'

    def get_object(self, queryset=None):
        return get_object_or_404(Vacancies, slug=self.kwargs['vacancy_slug'])
