from django.db import models


class ProductStatus(models.TextChoices):
    """Статусы для товара"""
    IN_STOCK = 'in_stock', 'В наличии'
    TO_ORDER = 'to_order', 'Под заказ'


class ProductColour(models.TextChoices):
    """Статусы для товара"""
    BLUE = 'blue', 'Синий'
    GREEN = 'green', 'Зеленый'
