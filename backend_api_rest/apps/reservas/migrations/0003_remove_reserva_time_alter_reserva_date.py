# Generated by Django 4.1.1 on 2022-11-04 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='time',
        ),
        migrations.AlterField(
            model_name='reserva',
            name='date',
            field=models.DateTimeField(verbose_name='Fecha'),
        ),
    ]
