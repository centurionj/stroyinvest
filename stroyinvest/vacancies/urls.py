from django.urls import path

from . import views

urlpatterns = [
    path('', views.VacanciesListView.as_view(), name='vacancies'),
    path('<slug:vacancy_slug>/', views.VacancyDetailView.as_view(), name='vacancy_detail'),
]
