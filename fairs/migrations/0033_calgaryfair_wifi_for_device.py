# Generated by Django 2.1.5 on 2019-02-27 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fairs', '0032_remove_edmontonfair_additional_breakfast_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='calgaryfair',
            name='wifi_for_device',
            field=models.CharField(default='-', max_length=400),
        ),
    ]