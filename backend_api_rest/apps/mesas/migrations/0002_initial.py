# Generated by Django 4.1.1 on 2022-10-13 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mesas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesa',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario ID'),
        ),
    ]
