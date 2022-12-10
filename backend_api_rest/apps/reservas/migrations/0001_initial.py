# Generated by Django 4.1.1 on 2022-12-10 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mesas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=100, verbose_name='Estado')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('time', models.TimeField(verbose_name='Time')),
                ('date_reserva', models.DateTimeField(verbose_name='Fecha y Hora')),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservas_mesa', to='mesas.mesa', verbose_name='Mesa ID')),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
            },
        ),
    ]
