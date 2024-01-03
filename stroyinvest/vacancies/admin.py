from django.contrib import admin

from common.admin_mixin import CKMixin
from vacancies.models import Vacancies


@admin.register(Vacancies)
class VacanciesAdmin(CKMixin, admin.ModelAdmin):
    list_display = ('title',)
