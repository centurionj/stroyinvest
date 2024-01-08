from django.db import models

from autoslug import AutoSlugField

from common.model_mixin import ModelMixin


class Vacancies(ModelMixin, models.Model):
    """Модель вакансий"""
    url_name = 'vacancy_detail'

    title = models.CharField('Заголовок', max_length=55)
    content = models.TextField('Описание')
    slug = AutoSlugField(populate_from='title', unique=True, editable=False)

    class Meta:
        verbose_name_plural = 'Вакансии'
        verbose_name = 'Вакансия'

    def __str__(self):
        return self.title
