# Generated by Django 4.1.1 on 2022-11-04 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='end_time',
            field=models.DateTimeField(verbose_name='Hora Termino'),
        ),
        migrations.AlterField(
            model_name='orden',
            name='start_time',
            field=models.DateTimeField(verbose_name='Hora Inicio'),
        ),
    ]
