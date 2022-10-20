# Generated by Django 4.1.1 on 2022-10-18 23:23

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
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mesas.mesa', verbose_name='Mesa ID')),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
            },
        ),
    ]
