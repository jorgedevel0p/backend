# Generated by Django 4.1.1 on 2022-11-03 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ordenes', '0001_initial'),
        ('detalle_ordenes', '0001_initial'),
        ('platos', '0001_initial'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleorden',
            name='orden',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ordenes.orden', verbose_name='Orden ID'),
        ),
        migrations.AddField(
            model_name='detalleorden',
            name='plato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalle_ordenes_plato', to='platos.plato', verbose_name='Plato ID'),
        ),
        migrations.AddField(
            model_name='detalleorden',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalle_ordenes_producto', to='productos.producto', verbose_name='Producto ID'),
        ),
    ]
