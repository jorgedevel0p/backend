# Generated by Django 4.1.1 on 2022-09-23 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='measure_unit',
            field=models.CharField(max_length=50, verbose_name='Unidad de Medida'),
        ),
    ]
