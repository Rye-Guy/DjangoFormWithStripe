from cfcapp.models import SalesFormData
from django.db import models

class TorontoFair(models.Model):

    related_sale = models.ForeignKey(SalesFormData, on_delete=models.SET_NULL, null=True)
    date_selection = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    toronto_booth_option = models.CharField(max_length=100, default='-')
    toronto_additional_booth_option = models.CharField(max_length=400, default='-')
    fair_total_spent = models.DecimalField(max_digits=7, decimal_places=2, blank=False, default=0.00)
    special_request = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        date_string = self.date_selection
        related_company = self.related_sale.company_name
        return related_company + " For: " + date_string + " TOR"


class CalgaryFair(models.Model):

    related_sale = models.ForeignKey(SalesFormData, on_delete=models.SET_NULL, null=True)
    date_selection = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    calgary_booth_option = models.CharField(max_length=100, default='-')
    calgary_additional_booth_option = models.CharField(max_length=400, default='-')
    calgary_additional_lunch_option = models.CharField(max_length=400, default='-')
    calgary_diet_request = models.CharField(max_length=400, blank=True, default='')
    calgary_venue_options = models.CharField(max_length=255, blank=False, default='-')
    fair_total_spent = models.DecimalField(max_digits=7, decimal_places=2, blank=False, default=0.00)
    special_request = models.TextField(max_length=2000, blank=True)


    def __str__(self):
        date_string = self.date_selection
        related_company = self.related_sale.company_name
        return str(related_company) + " For: " + date_string + " CAL"

class EdmontonFair(models.Model):

    related_sale = models.ForeignKey(SalesFormData, on_delete=models.SET_NULL, null=True)
    date_selection = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    edmonton_booth_option = models.CharField(max_length=100, default='-')
    edmonton_additional_booth_option = models.CharField(max_length=400, default='-')
    edmonton_additional_lunch_option = models.CharField(max_length=400, default='-')
    edmonton_additional_breakfast_option = models.CharField(max_length=400, default='-')
    edmonton_diet_request = models.CharField(max_length=400, blank=True, default='')
    edmonton_venue_options = models.CharField(max_length=255, blank=False, default='-')
    fair_total_spent = models.DecimalField(max_digits=7, decimal_places=2, blank=False, default=0.00)
    special_request = models.TextField(max_length=2000, blank=True)


    def __str__(self):
        date_string = self.date_selection
        related_company = self.related_sale.company_name
        return str(related_company) + " For: " + date_string + " EDM"


class WinnipegFair(models.Model):

    related_sale = models.ForeignKey(SalesFormData, on_delete=models.SET_NULL, null=True)
    date_selection = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    winnipeg_booth_option = models.CharField(max_length=100, default='-')
    winnipeg_additional_booth_option = models.CharField(max_length=400, default='-')
    winnipeg_additional_lunch_option = models.CharField(max_length=400, default='-')
    winnipeg_diet_request = models.CharField(max_length=400, blank=True, default='')
    fair_total_spent = models.DecimalField(max_digits=7, decimal_places=2, blank=False, default=0.00)
    special_request = models.TextField(max_length=2000, blank=True)


    def __str__(self):
        date_string = self.date_selection
        related_company = self.related_sale.company_name
        return str(related_company) + " For: " + date_string + " WPG"