from cfcapp.models import SalesFormData
from django.db import models

class TorontoFair(models.Model):
    related_sale = models.ForeignKey(SalesFormData, on_delete=models.SET_NULL, null=True)
    toronto_dates = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    toronto_date_1 = models.CharField(max_length=400, blank=True, default='-')
    toronto_date_2 = models.CharField(max_length=400, blank=True, default='-')
    toronto_booth_option_1 = models.CharField(max_length=100, default='-')
    toronto_booth_option_2 = models.CharField(max_length=100, default='-')
    toronto_additional_booth_option_1 = models.CharField(max_length=400, default='-')
    toronto_additional_booth_option_2 = models.CharField(max_length=400, default='-')

class CalgaryFair(models.Model):
    related_sale = models.ForeignKey(SalesFormData, on_delete=models.SET_NULL, null=True)
    calgary_dates = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    calgary_booth_option_1 = models.CharField(max_length=100, default='-')
    calgary_booth_option_2 = models.CharField(max_length=100, default='-')
    calgary_booth_option_3 = models.CharField(max_length=100, default='-')
    calgary_date_1 = models.CharField(max_length=400, blank=True, default='-')
    calgary_date_2 = models.CharField(max_length=400, blank=True, default='-')
    calgary_date_3 = models.CharField(max_length=400, blank=True, default='-')
    calgary_additional_booth_option_1 = models.CharField(max_length=400, default='-')
    calgary_additional_booth_option_2 = models.CharField(max_length=400, default='-')
    calgary_additional_booth_option_3 = models.CharField(max_length=400, default='-')
    calgary_additional_lunch_option_1 = models.CharField(max_length=400, default='-')
    calgary_additional_lunch_option_2 = models.CharField(max_length=400, default='-')
    calgary_additional_lunch_option_3 = models.CharField(max_length=400, default='-')
    calgary_diet_request_1 = models.CharField(max_length=400, blank=True, default='')
    calgary_diet_request_2 = models.CharField(max_length=400, blank=True, default='')
    calgary_diet_request_3 = models.CharField(max_length=400, blank=True, default='')
    calgary_venue_options = models.CharField(max_length=255, blank=False, default='-')

class EdmontonFair(models.Model):
    related_sale = models.ForeignKey(SalesFormData, on_delete=models.SET_NULL, null=True)
    edmonton_dates = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    edmonton_date_1 = models.CharField(max_length=400, blank=True, default='-')
    edmonton_date_2 = models.CharField(max_length=400, blank=True, default='-')
    edmonton_date_3 = models.CharField(max_length=400, blank=True, default='-')
    edmonton_date_4 = models.CharField(max_length=400, blank=True, default='-')
    edmonton_booth_option_1 = models.CharField(max_length=100, default='-')
    edmonton_booth_option_2 = models.CharField(max_length=100, default='-')
    edmonton_booth_option_3 = models.CharField(max_length=100, default='-')
    edmonton_booth_option_4 = models.CharField(max_length=100, default='-')
    edmonton_additional_booth_option_1 = models.CharField(max_length=400, default='-')
    edmonton_additional_booth_option_2 = models.CharField(max_length=400, default='-')
    edmonton_additional_booth_option_3 = models.CharField(max_length=400, default='-')
    edmonton_additional_booth_option_4 = models.CharField(max_length=400, default='-')
    edmonton_additional_lunch_option_1 = models.CharField(max_length=400, default='-')
    edmonton_additional_lunch_option_2 = models.CharField(max_length=400, default='-')
    edmonton_additional_lunch_option_3 = models.CharField(max_length=400, default='-')
    edmonton_additional_lunch_option_4 = models.CharField(max_length=400, default='-')
    edmonton_additional_breakfast_option_1 = models.CharField(max_length=400, default='-')
    edmonton_additional_breakfast_option_2 = models.CharField(max_length=400, default='-')
    edmonton_additional_breakfast_option_3 = models.CharField(max_length=400, default='-')
    edmonton_additional_breakfast_option_4 = models.CharField(max_length=400, default='-')
    edmonton_diet_request_1 = models.CharField(max_length=400, blank=True, default='')
    edmonton_diet_request_2 = models.CharField(max_length=400, blank=True, default='')
    edmonton_diet_request_3 = models.CharField(max_length=400, blank=True, default='')
    edmonton_diet_request_4 = models.CharField(max_length=400, blank=True, default='')
    edmonton_venue_options = models.CharField(max_length=255, blank=False, default='-')
'''
0 WinnipegFair object (6)
1 ['04-02-2019', '07-10-2019', '07-23-2019']
2 04-02-2019
3 07-10-2019
4 07-23-2019
5 2495
6 1995
7 1495
8 1
9 2
10 3
11 1
12 2
13 3
14 Eggs
15 Meat
16 Jerry

'''
class WinnipegFair(models.Model):
    related_sale = models.ForeignKey(SalesFormData, on_delete=models.SET_NULL, null=True)
    winnipeg_dates = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    winnipeg_date_1 = models.CharField(max_length=400, blank=True, default='-')
    winnipeg_date_2 = models.CharField(max_length=400, blank=True, default='-')
    winnipeg_date_3 = models.CharField(max_length=400, blank=True, default='-')
    winnipeg_booth_option_1 = models.CharField(max_length=100, default='-')
    winnipeg_booth_option_2 = models.CharField(max_length=100, default='-')
    winnipeg_booth_option_3 = models.CharField(max_length=100, default='-')
    winnipeg_additional_booth_option_1 = models.CharField(max_length=400, default='-')
    winnipeg_additional_booth_option_2 = models.CharField(max_length=400, default='-')
    winnipeg_additional_booth_option_3 = models.CharField(max_length=400, default='-')
    winnipeg_additional_lunch_option_1 = models.CharField(max_length=400, default='-')
    winnipeg_additional_lunch_option_2 = models.CharField(max_length=400, default='-')
    winnipeg_additional_lunch_option_3 = models.CharField(max_length=400, default='-')
    winnipeg_diet_request_1 = models.CharField(max_length=400, blank=True, default='')
    winnipeg_diet_request_2 = models.CharField(max_length=400, blank=True, default='')
    winnipeg_diet_request_3 = models.CharField(max_length=400, blank=True, default='')