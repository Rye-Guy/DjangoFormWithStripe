# Generated by Django 2.1.5 on 2019-02-21 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fairs', '0028_torontofair_tax_to_charge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calgaryfair',
            name='booth_cost',
        ),
        migrations.RemoveField(
            model_name='calgaryfair',
            name='fair_total_spent',
        ),
        migrations.AddField(
            model_name='calgaryfair',
            name='discount_cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=7),
        ),
        migrations.AddField(
            model_name='calgaryfair',
            name='grand_total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=7),
        ),
        migrations.AddField(
            model_name='calgaryfair',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
        migrations.AddField(
            model_name='calgaryfair',
            name='tax_to_charge',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=7),
        ),
    ]
