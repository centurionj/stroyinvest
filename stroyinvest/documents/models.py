from django.db import models
from autoslug import AutoSlugField

class Document(models.Model):
    """Модель для документов"""
    title = models.CharField('Название документа', max_length=100)
    file = models.FileField('Документ', upload_to='documents')
    slug = AutoSlugField(populate_from='title', unique=True, editable=False)

    class Meta:
        verbose_name_plural = 'Документы'
        verbose_name = 'Документ'