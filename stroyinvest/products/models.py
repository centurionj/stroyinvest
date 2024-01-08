from django.db import models

from autoslug import AutoSlugField
from django.urls import reverse

from products.enums import ProductStatus, ProductColour
from service.models import Service
from common.model_mixin import ModelMixin


class ProductCategory(models.Model):
    """Модель категории"""
    title = models.CharField('Категория товара', max_length=55)

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    def __str__(self):
        return self.title


class Product(ModelMixin, models.Model):
    """Модель продукта"""
    url_name = 'product-detail'

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
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='category')
    services = models.ManyToManyField(Service, related_name='products')
    slug = AutoSlugField(populate_from='title', unique=True, editable=False)
    colour = models.CharField(
        max_length=50,
        choices=ProductColour.choices,
        verbose_name="Цвет статуса",
        null=True, blank=True
    )

    def _check_status(self):
        """Проверка статуса товара и установка цвета фона"""
        if self.status == ProductStatus.IN_STOCK:
            self.colour = ProductColour.GREEN
        else:
            self.colour = ProductColour.BLUE

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self._check_status()
        super(Product, self).save(*args, **kwargs)
