# Generated by Django 4.1.1 on 2022-09-23 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='category_product',
            field=models.CharField(max_length=50, verbose_name='Categoría de Producto'),
        ),
    ]
