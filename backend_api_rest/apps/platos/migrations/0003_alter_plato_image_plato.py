# Generated by Django 4.1.1 on 2022-12-06 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platos', '0002_alter_plato_image_plato_alter_plato_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plato',
            name='image_plato',
            field=models.CharField(max_length=450),
        ),
    ]
