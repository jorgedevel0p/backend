# Generated by Django 4.1.1 on 2022-10-14 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_type_user_type_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='type_user',
            new_name='type',
        ),
    ]
