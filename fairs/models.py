from cfcapp.models import SalesFormData
from django.db import models

class OnSiteContacts(models.Model):

    name = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=300)
    email = models.CharField(max_length=300)



class TorontoFair(models.Model):

    related_sale = models.ForeignKey(SalesFormData, on_delete=models.SET_NULL, null=True)
    booth_id = models.IntegerField(blank=True, null=True)
    account_number = models.CharField(max_length=10, blank=True)
    date_selection = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    booth_option = models.CharField(max_length=100, default='-')
    booth_cost = models.CharField(max_length=100, blank=True)
    additional_booth_option = models.CharField(max_length=400, default='-')
    fair_total_spent = models.DecimalField(max_digits=7, decimal_places=2, blank=False, default=0.00)
    special_request = models.TextField(max_length=2000, blank=True)
    contact = models.ForeignKey(OnSiteContacts, on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        date_string = self.date_selection
        related_company = self.related_sale.company_name
        return related_company + " For: " + date_string + " TOR"

    def booth_cost_cal(self):
        boothOptWithDiscount = self.booth_option / self.related_sale.discount_percentage
        return boothOptWithDiscount

    def related_class(self):
        return 'toronto'

class CalgaryFair(models.Model):

    related_sale = models.ForeignKey(SalesFormData, on_delete=models.SET_NULL, null=True)
    date_selection = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    booth_option = models.CharField(max_length=100, default='-')
    additional_booth_option = models.CharField(max_length=400, default='-')
    additional_lunch_option = models.CharField(max_length=400, default='-')
    diet_request = models.CharField(max_length=400, blank=True, default='')
    wifi = models.BooleanField(default=False)
    electricity = models.BooleanField(default=False)
    fair_total_spent = models.DecimalField(max_digits=7, decimal_places=2, blank=False, default=0.00)
    special_request = models.TextField(max_length=2000, blank=True)
    booth_id = models.IntegerField(blank=True, null=True)
    account_number = models.CharField(max_length=10, blank=True)
    booth_cost = models.CharField(max_length=100, blank=True)
    contact = models.ForeignKey(OnSiteContacts, on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        date_string = self.date_selection
        related_company = self.related_sale.company_name
        return str(related_company) + " For: " + date_string + " CAL"

    def related_class(self):
        return 'calgary'

class EdmontonFair(models.Model):

    related_sale = models.ForeignKey(SalesFormData, on_delete=models.SET_NULL, null=True)
    date_selection = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    booth_option = models.CharField(max_length=100, default='-')
    additional_booth_option = models.CharField(max_length=400, default='-')
    additional_lunch_option = models.CharField(max_length=400, default='-')
    additional_breakfast_option = models.CharField(max_length=400, default='-')
    wifi = models.BooleanField(default=False)
    electricity = models.BooleanField(default=False)
    diet_request = models.CharField(max_length=400, blank=True, default='')
    fair_total_spent = models.DecimalField(max_digits=7, decimal_places=2, blank=False, default=0.00)
    special_request = models.TextField(max_length=2000, blank=True)
    booth_id = models.IntegerField(blank=True, null=True)
    account_number = models.CharField(max_length=10, blank=True)
    booth_cost = models.CharField(max_length=100, blank=True)
    contact = models.ForeignKey(OnSiteContacts, on_delete=models.SET_NULL, blank=True, null=True)



    def __str__(self):
        date_string = self.date_selection
        related_company = self.related_sale.company_name
        return str(related_company) + " For: " + date_string + " EDM"

    def related_class(self):
        return 'edmonton'


class WinnipegFair(models.Model):

    related_sale = models.ForeignKey(SalesFormData, on_delete=models.SET_NULL, null=True)
    date_selection = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    booth_option = models.CharField(max_length=100, default='-')
    additional_booth_option = models.CharField(max_length=400, default='-')
    additional_lunch_option = models.CharField(max_length=400, default='-')
    diet_request = models.CharField(max_length=400, blank=True, default='')
    fair_total_spent = models.DecimalField(max_digits=7, decimal_places=2, blank=False, default=0.00)
    special_request = models.TextField(max_length=2000, blank=True)
    booth_id = models.IntegerField(blank=True, null=True)
    account_number = models.CharField(max_length=10, blank=True)
    booth_cost = models.CharField(max_length=100, blank=True)
    contact = models.ForeignKey(OnSiteContacts, on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        date_string = self.date_selection
        related_company = self.related_sale.company_name
        return str(related_company) + " For: " + date_string + " WPG"
