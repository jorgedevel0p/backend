# Generated by Django 4.1.1 on 2022-10-05 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ordenes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('value', models.PositiveIntegerField(verbose_name='Valor')),
                ('tip', models.PositiveIntegerField(verbose_name='Propina')),
                ('payment_method', models.CharField(max_length=150, verbose_name='Método de Pago')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('time', models.TimeField(verbose_name='Hora')),
                ('state', models.CharField(max_length=150, verbose_name='Estado de Pago')),
                ('orden_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordenes.orden', verbose_name='Orden ID')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario ID')),
            ],
            options={
                'verbose_name': 'Boleta',
                'verbose_name_plural': 'Boletas',
            },
        ),
    ]
