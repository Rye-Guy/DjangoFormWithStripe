# Generated by Django 2.1.5 on 2019-01-28 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cfcapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalgaryFair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calgary_dates', models.CharField(blank=True, default='Value Determined By Checkbox', max_length=400)),
                ('calgary_booth_options', models.CharField(blank=True, default='Value Determined By Checkbox', max_length=400)),
                ('calgary_options', models.CharField(blank=True, default='Value Determined By Checkbox', max_length=400)),
                ('calgary_date_1', models.CharField(blank=True, default='-', max_length=400)),
                ('calgary_date_2', models.CharField(blank=True, default='-', max_length=400)),
                ('calgary_date_3', models.CharField(blank=True, default='-', max_length=400)),
                ('calgary_additional_booth_option_1', models.CharField(default='-', max_length=400)),
                ('calgary_additional_booth_option_2', models.CharField(default='-', max_length=400)),
                ('calgary_additional_booth_option_3', models.CharField(default='-', max_length=400)),
                ('calgary_additional_lunch_option_1', models.CharField(default='-', max_length=400)),
                ('calgary_additional_lunch_option_2', models.CharField(default='-', max_length=400)),
                ('calgary_additional_lunch_option_3', models.CharField(default='-', max_length=400)),
                ('calgary_diet_request_1', models.CharField(blank=True, default='', max_length=400)),
                ('calgary_diet_request_2', models.CharField(blank=True, default='', max_length=400)),
                ('calgary_diet_request_3', models.CharField(blank=True, default='', max_length=400)),
                ('calgary_venue_options', models.CharField(default='-', max_length=255)),
                ('related_sale', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cfcapp.SalesFormData')),
            ],
        ),
        migrations.CreateModel(
            name='EdmontonFair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edmonton_dates', models.CharField(blank=True, default='Value Determined By Checkbox', max_length=400)),
                ('edmonton_booth_options', models.CharField(blank=True, default='Value Determined By Checkbox', max_length=400)),
                ('edmonton_date_1', models.CharField(blank=True, default='-', max_length=400)),
                ('edmonton_date_2', models.CharField(blank=True, default='-', max_length=400)),
                ('edmonton_date_3', models.CharField(blank=True, default='-', max_length=400)),
                ('edmonton_date_4', models.CharField(blank=True, default='-', max_length=400)),
                ('edmonton_additional_booth_option_1', models.CharField(default='-', max_length=400)),
                ('edmonton_additional_booth_option_2', models.CharField(default='-', max_length=400)),
                ('edmonton_additional_booth_option_3', models.CharField(default='-', max_length=400)),
                ('edmonton_additional_booth_option_4', models.CharField(default='-', max_length=400)),
                ('edmonton_additional_lunch_option_1', models.CharField(default='-', max_length=400)),
                ('edmonton_additional_lunch_option_2', models.CharField(default='-', max_length=400)),
                ('edmonton_additional_lunch_option_3', models.CharField(default='-', max_length=400)),
                ('edmonton_additional_lunch_option_4', models.CharField(default='-', max_length=400)),
                ('edmonton_additional_breakfast_option_1', models.CharField(default='-', max_length=400)),
                ('edmonton_additional_breakfast_option_2', models.CharField(default='-', max_length=400)),
                ('edmonton_additional_breakfast_option_3', models.CharField(default='-', max_length=400)),
                ('edmonton_additional_breakfast_option_4', models.CharField(default='-', max_length=400)),
                ('edmonton_diet_request_1', models.CharField(blank=True, default='', max_length=400)),
                ('edmonton_diet_request_2', models.CharField(blank=True, default='', max_length=400)),
                ('edmonton_diet_request_3', models.CharField(blank=True, default='', max_length=400)),
                ('edmonton_diet_request_4', models.CharField(blank=True, default='', max_length=400)),
                ('edmonton_venue_options', models.CharField(default='-', max_length=255)),
                ('related_sale', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cfcapp.SalesFormData')),
            ],
        ),
        migrations.CreateModel(
            name='TorontoFair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toronto_dates', models.CharField(blank=True, default='Value Determined By Checkbox', max_length=400)),
                ('toronto_booth_options', models.CharField(blank=True, default='Value Determined By Checkbox', max_length=400)),
                ('toronto_date_1', models.CharField(blank=True, default='-', max_length=400)),
                ('toronto_date_2', models.CharField(blank=True, default='-', max_length=400)),
                ('toronto_additional_booth_option_1', models.CharField(default='-', max_length=400)),
                ('toronto_additional_booth_option_2', models.CharField(default='-', max_length=400)),
                ('related_sale', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cfcapp.SalesFormData')),
            ],
        ),
        migrations.CreateModel(
            name='WinnipegFair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winnipeg_dates', models.CharField(blank=True, default='Value Determined By Checkbox', max_length=400)),
                ('winnipeg_booth_options', models.CharField(blank=True, default='Value Determined By Checkbox', max_length=400)),
                ('winnipeg_date_1', models.CharField(blank=True, default='-', max_length=400)),
                ('winnipeg_date_2', models.CharField(blank=True, default='-', max_length=400)),
                ('winnipeg_date_3', models.CharField(blank=True, default='-', max_length=400)),
                ('winnipeg_additional_booth_option_1', models.CharField(default='-', max_length=400)),
                ('winnipeg_additional_booth_option_2', models.CharField(default='-', max_length=400)),
                ('winnipeg_additional_booth_option_3', models.CharField(default='-', max_length=400)),
                ('winnipeg_additional_lunch_option_1', models.CharField(default='-', max_length=400)),
                ('winnipeg_additional_lunch_option_2', models.CharField(default='-', max_length=400)),
                ('winnipeg_additional_lunch_option_3', models.CharField(default='-', max_length=400)),
                ('winnipeg_diet_request_1', models.CharField(blank=True, default='', max_length=400)),
                ('winnipeg_diet_request_2', models.CharField(blank=True, default='', max_length=400)),
                ('winnipeg_diet_request_3', models.CharField(blank=True, default='', max_length=400)),
                ('related_sale', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cfcapp.SalesFormData')),
            ],
        ),
    ]