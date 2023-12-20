from django.db import models


class Question(models.Model):
    """Модель заявки клиента"""
    name = models.CharField('Имя', max_length=55)
    phone = models.CharField('Телефон', max_length=12)
    email = models.EmailField('Почта')
    message = models.TextField('Сообщение')

    class Meta:
        verbose_name_plural = 'Заявки'
        verbose_name = 'Заявка'
