# Generated by Django 2.1.5 on 2019-02-14 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fairs', '0021_auto_20190214_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='onsitecontacts',
            name='contact_calgary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fairs.CalgaryFair'),
        ),
        migrations.AddField(
            model_name='onsitecontacts',
            name='contact_edmonton',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fairs.EdmontonFair'),
        ),
        migrations.AddField(
            model_name='onsitecontacts',
            name='contact_toronto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fairs.TorontoFair'),
        ),
        migrations.AddField(
            model_name='onsitecontacts',
            name='contact_winnipeg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fairs.WinnipegFair'),
        ),
    ]
