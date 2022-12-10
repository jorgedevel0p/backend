# Generated by Django 4.1.1 on 2022-12-10 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleOrden',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('number_dish', models.PositiveIntegerField(verbose_name='Cantidad de Platos')),
            ],
            options={
                'verbose_name': 'Detalle Orden',
                'verbose_name_plural': 'Detalle Ordenes',
            },
        ),
    ]
