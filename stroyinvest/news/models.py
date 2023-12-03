from django.db import models
from django.utils import timezone

from autoslug import AutoSlugField


class News(models.Model):
    title = models.CharField('Заголовок', max_length=55)
    content = models.TextField('Контент новости')
    date = models.DateTimeField('Дата', null=True, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True, editable=False)

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'

    def save(self, *args, **kwargs):
        if not self.date:
            self.date = timezone.now()
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
