from django.db import models


class Icon(models.Model):
    icon = models.ImageField('Фото услуги', upload_to='service_icon')

    class Meta:
        verbose_name_plural = 'Иконки'
        verbose_name = 'Иконка'

    def __str__(self):
        return self.icon

class Service(models.Model):
    photo = models.ImageField('Фото услуги', upload_to='service_photo')
    icon = models.ForeignKey(Icon, on_delete=models.PROTECT, related_name='icons')
    title = models.CharField('Название услуги', max_length=100)
    description = models.TextField('Описание услуги')

    class Meta:
        verbose_name_plural = 'Услуги'
        verbose_name = 'Услуга'

    def __str__(self):
        return self.title
