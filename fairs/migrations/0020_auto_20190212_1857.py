# Generated by Django 2.1.5 on 2019-02-12 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fairs', '0019_auto_20190212_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calgaryfair',
            name='contact',
            field=models.ManyToManyField(blank=True, to='fairs.OnSiteContacts'),
        ),
        migrations.AlterField(
            model_name='edmontonfair',
            name='contact',
            field=models.ManyToManyField(blank=True, to='fairs.OnSiteContacts'),
        ),
        migrations.AlterField(
            model_name='torontofair',
            name='contact',
            field=models.ManyToManyField(blank=True, to='fairs.OnSiteContacts'),
        ),
        migrations.AlterField(
            model_name='winnipegfair',
            name='contact',
            field=models.ManyToManyField(blank=True, to='fairs.OnSiteContacts'),
        ),
    ]