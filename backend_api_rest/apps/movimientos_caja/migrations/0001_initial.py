# Generated by Django 4.1.1 on 2022-10-26 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boletas', '0001_initial'),
        ('facturas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovimientoCaja',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('date_mov', models.DateField(verbose_name='Fecha Movimiento')),
                ('initial_balance', models.IntegerField(verbose_name='Saldo Inicial')),
                ('boleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boletas.boleta', verbose_name='Boleta ID')),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturas.factura', verbose_name='Factura ID')),
            ],
            options={
                'verbose_name': 'Movimiento Caja',
                'verbose_name_plural': 'Movimientos Caja',
            },
        ),
    ]
