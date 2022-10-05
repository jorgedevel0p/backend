# Generated by Django 4.1.1 on 2022-10-05 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='Nombre Proveedor')),
                ('email', models.EmailField(max_length=150, verbose_name='Mail Proveedor')),
                ('phone', models.CharField(max_length=12, verbose_name='Telefono Proveedor')),
                ('state', models.BooleanField(default=True, verbose_name='Estado Proveedor')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
    ]
