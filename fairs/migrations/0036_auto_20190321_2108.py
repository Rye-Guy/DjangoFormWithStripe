# Generated by Django 2.1.5 on 2019-03-21 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fairs', '0035_auto_20190321_2024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calgaryfair',
            old_name='special_request',
            new_name='notes',
        ),
        migrations.RenameField(
            model_name='edmontonfair',
            old_name='special_request',
            new_name='notes',
        ),
        migrations.RenameField(
            model_name='torontofair',
            old_name='special_request',
            new_name='notes',
        ),
        migrations.RenameField(
            model_name='winnipegfair',
            old_name='special_request',
            new_name='notes',
        ),
    ]
