# Generated by Django 2.1.5 on 2019-01-30 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fairs', '0003_auto_20190130_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='winnipegfair',
            name='winnipeg_booth_options',
        ),
    ]
