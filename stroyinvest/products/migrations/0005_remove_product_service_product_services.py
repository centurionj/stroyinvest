# Generated by Django 4.2.7 on 2023-12-11 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
        ('products', '0004_alter_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='service',
        ),
        migrations.AddField(
            model_name='product',
            name='services',
            field=models.ManyToManyField(related_name='products', to='service.service'),
        ),
    ]
