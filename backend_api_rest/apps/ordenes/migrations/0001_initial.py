# Generated by Django 4.1.1 on 2022-10-26 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mesas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='Fecha')),
                ('time', models.TimeField(verbose_name='Hora')),
                ('number_people', models.PositiveIntegerField(verbose_name='Número de Personas')),
                ('state', models.BooleanField(default=True, verbose_name='Disponibilidad')),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mesas.mesa', verbose_name='Mesa ID')),
            ],
            options={
                'verbose_name': 'Orden',
                'verbose_name_plural': 'Ordenes',
            },
        ),
    ]
