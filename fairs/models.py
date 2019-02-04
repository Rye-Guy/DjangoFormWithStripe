from cfcapp.models import SalesFormData
from django.db import models

class TorontoFair(models.Model):
    related_sale = models.ForeignKey(SalesFormData, on_delete=models.SET_NULL, null=True)
    toronto_date_selection = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    toronto_booth_option = models.CharField(max_length=100, default='-')
    toronto_additional_booth_option = models.CharField(max_length=400, default='-')

class CalgaryFair(models.Model):
    related_sale = models.ForeignKey(SalesFormData, on_delete=models.SET_NULL, null=True)
    calgary_date_selection = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    calgary_booth_option = models.CharField(max_length=100, default='-')
    calgary_additional_booth_option = models.CharField(max_length=400, default='-')
    calgary_additional_lunch_option = models.CharField(max_length=400, default='-')
    calgary_diet_request = models.CharField(max_length=400, blank=True, default='')
    calgary_venue_options = models.CharField(max_length=255, blank=False, default='-')

class EdmontonFair(models.Model):
    related_sale = models.ForeignKey(SalesFormData, on_delete=models.SET_NULL, null=True)
    edmonton_date_selection = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    edmonton_booth_option = models.CharField(max_length=100, default='-')
    edmonton_additional_booth_option = models.CharField(max_length=400, default='-')
    edmonton_additional_lunch_option = models.CharField(max_length=400, default='-')
    edmonton_additional_breakfast_option = models.CharField(max_length=400, default='-')
    edmonton_diet_request = models.CharField(max_length=400, blank=True, default='')
    edmonton_venue_options = models.CharField(max_length=255, blank=False, default='-')

class WinnipegFair(models.Model):
    related_sale = models.ForeignKey(SalesFormData, on_delete=models.SET_NULL, null=True)
    winnipeg_date_selection = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    winnipeg_booth_option = models.CharField(max_length=100, default='-')
    winnipeg_additional_booth_option = models.CharField(max_length=400, default='-')
    winnipeg_additional_lunch_option = models.CharField(max_length=400, default='-')
    winnipeg_diet_request = models.CharField(max_length=400, blank=True, default='')