from django.db import models
from autoslug import AutoSlugField

class Icon(models.Model):
    icon = models.TextField('Иконка услуги')

    class Meta:
        verbose_name_plural = 'Иконки'
        verbose_name = 'Иконка'


class Service(models.Model):
    photo = models.ImageField('Фото услуги', upload_to='service_photo')
    icon = models.ForeignKey(Icon, on_delete=models.PROTECT, related_name='icons')
    title = models.CharField('Название услуги', max_length=100)
    description = models.TextField('Описание услуги')
    slug = AutoSlugField(populate_from='title', unique=True, editable=False)

    class Meta:
        verbose_name_plural = 'Услуги'
        verbose_name = 'Услуга'

    def __str__(self):
        return self.title