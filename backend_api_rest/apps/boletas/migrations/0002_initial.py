# Generated by Django 4.1.1 on 2022-10-18 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boletas', '0001_initial'),
        ('ordenes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boleta',
            name='orden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boletas', to='ordenes.orden', verbose_name='Orden ID'),
        ),
    ]
