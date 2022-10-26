# Generated by Django 4.1.1 on 2022-10-26 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proveedores', '0001_initial'),
        ('pedidos_proveedor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='Fecha Facturación')),
                ('pedido_proveedor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pedidos_proveedor.pedidoproveedor', verbose_name=' Pedido Proveedor ID')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.proveedor', verbose_name='Proveedor ID')),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
            },
        ),
    ]
