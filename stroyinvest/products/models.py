from django.core.validators import MinValueValidator
from django.db import models

from autoslug import AutoSlugField

from .enums import ProductStatus
from attendance.models import Service


class Brand(models.Model):
    title = models.CharField('Название брэнда', max_length=55)

    class Meta:
        verbose_name_plural = 'Брэнды'
        verbose_name = 'Брэнд'

    def __str__(self):
        return self.title


class Product(models.Model):
    photo = models.ImageField('Фото товара', upload_to='products_photo')
    title = models.CharField('Название товара', max_length=255)
    description = models.TextField('Описание товара')
    status = models.CharField(
        max_length=50,
        choices=ProductStatus.choices,
        default=ProductStatus.IN_STOCK,
        verbose_name="Статус товара",
        null=True, blank=True
    )
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    old_price = models.DecimalField(
        'Цена',
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        null=True, blank=True
    )
    articul = models.CharField('Артикул', max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brands')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='services')
    slug = AutoSlugField(populate_from='title', unique=True, editable=False)

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'

    def __str__(self):
        return self.title