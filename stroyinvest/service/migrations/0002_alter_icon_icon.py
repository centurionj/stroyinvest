# Generated by Django 4.2.7 on 2023-12-04 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icon',
            name='icon',
            field=models.ImageField(upload_to='icons', verbose_name='Фото услуги'),
        ),
    ]