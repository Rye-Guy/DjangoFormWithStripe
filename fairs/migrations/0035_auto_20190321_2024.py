# Generated by Django 2.1.5 on 2019-03-21 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fairs', '0034_auto_20190228_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calgaryfair',
            name='diet_request',
        ),
        migrations.RemoveField(
            model_name='edmontonfair',
            name='diet_request',
        ),
        migrations.RemoveField(
            model_name='winnipegfair',
            name='diet_request',
        ),
    ]
