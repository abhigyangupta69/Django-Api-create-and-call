# Generated by Django 3.1.5 on 2021-01-20 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApplication', '0002_master'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Master',
            new_name='Student',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='author',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='title',
            new_name='last_name',
        ),
    ]
