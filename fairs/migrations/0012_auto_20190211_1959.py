# Generated by Django 2.1.5 on 2019-02-11 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fairs', '0011_auto_20190208_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='calgaryfair',
            name='special_request',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AddField(
            model_name='edmontonfair',
            name='special_request',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AddField(
            model_name='torontofair',
            name='special_request',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AddField(
            model_name='winnipegfair',
            name='special_request',
            field=models.TextField(blank=True, max_length=2000),
        ),
    ]