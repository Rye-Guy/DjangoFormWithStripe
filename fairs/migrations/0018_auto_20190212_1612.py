# Generated by Django 2.1.5 on 2019-02-12 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fairs', '0017_auto_20190212_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='calgaryfair',
            name='package_type',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='edmontonfair',
            name='package_type',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='torontofair',
            name='package_type',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='winnipegfair',
            name='package_type',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]