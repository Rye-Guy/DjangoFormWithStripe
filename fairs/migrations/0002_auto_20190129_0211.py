# Generated by Django 2.1.5 on 2019-01-29 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fairs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calgaryfair',
            name='calgary_booth_options',
        ),
        migrations.RemoveField(
            model_name='torontofair',
            name='toronto_booth_options',
        ),
        migrations.AddField(
            model_name='calgaryfair',
            name='calgary_booth_option_1',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AddField(
            model_name='calgaryfair',
            name='calgary_booth_option_2',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AddField(
            model_name='calgaryfair',
            name='calgary_booth_option_3',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AddField(
            model_name='edmontonfair',
            name='edmonton_booth_option_1',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AddField(
            model_name='edmontonfair',
            name='edmonton_booth_option_2',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AddField(
            model_name='edmontonfair',
            name='edmonton_booth_option_3',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AddField(
            model_name='edmontonfair',
            name='edmonton_booth_option_4',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AddField(
            model_name='torontofair',
            name='toronto_booth_option_1',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AddField(
            model_name='torontofair',
            name='toronto_booth_option_2',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AddField(
            model_name='winnipegfair',
            name='winnipeg_booth_option_1',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AddField(
            model_name='winnipegfair',
            name='winnipeg_booth_option_2',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AddField(
            model_name='winnipegfair',
            name='winnipeg_booth_option_3',
            field=models.CharField(default='-', max_length=100),
        ),
    ]
