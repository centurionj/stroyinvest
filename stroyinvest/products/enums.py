from django.db import models


class ProductStatus(models.TextChoices):
    """Статусы для товара"""
    IN_STOCK = 'in_stock', 'В наличии'
    TO_ORDER = 'to_order', 'Под заказ'