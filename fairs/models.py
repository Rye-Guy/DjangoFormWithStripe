from cfcapp.models import SalesFormData
from django.db import models

class OnSiteContacts(models.Model):

    name = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=300)
    email = models.CharField(max_length=300)

    def __str__(self):
        return self.name + " " + self.email



class TorontoFair(models.Model):

    related_sale = models.ForeignKey(SalesFormData, on_delete=models.SET_NULL, null=True)
    booth_id = models.IntegerField(blank=True, null=True)
    account_number = models.CharField(max_length=10, blank=True)
    date_selection = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    booth_option = models.CharField(max_length=100, default='-')
    package_type = models.CharField(max_length=100, blank=True)
    booth_cost = models.CharField(max_length=100, blank=True)
    additional_booth_option = models.CharField(max_length=400, default='-')
    fair_total_spent = models.DecimalField(max_digits=7, decimal_places=2, blank=False, default=0.00)
    special_request = models.TextField(max_length=2000, blank=True)
    contact = models.ManyToManyField(OnSiteContacts, blank=True)


    def __str__(self):
        date_string = self.date_selection
        related_company = self.related_sale.company_name
        return related_company + " For: " + date_string + " TOR"

    def booth_cost_cal(self):
        discount = self.related_sale.discount_percentage
        discount_dec = discount.replace('%', '.')
        boothDiscount = int(self.booth_option) * float(discount_dec)
        booth_cost = int(self.booth_option) - boothDiscount
        self.booth_cost = booth_cost
        self.save()
        return booth_cost

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
    package_type = models.CharField(max_length=100, blank=True)
    booth_cost = models.CharField(max_length=100, blank=True)
    contact = models.ManyToManyField(OnSiteContacts, blank=True)


    def __str__(self):
        date_string = self.date_selection
        related_company = self.related_sale.company_name
        return str(related_company) + " For: " + date_string + " CAL"

    def booth_cost_cal(self):
        discount = self.related_sale.discount_percentage
        discount_dec = discount.replace('%', '.')
        boothDiscount = int(self.booth_option) * float(discount_dec)
        booth_cost = int(self.booth_option) - boothDiscount
        self.booth_cost = booth_cost
        self.save()
        return booth_cost

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
    package_type = models.CharField(max_length=100, blank=True)
    booth_cost = models.CharField(max_length=100, blank=True)
    contact = models.ManyToManyField(OnSiteContacts, blank=True)



    def __str__(self):
        date_string = self.date_selection
        related_company = self.related_sale.company_name
        return str(related_company) + " For: " + date_string + " EDM"

    def booth_cost_cal(self):
        discount = self.related_sale.discount_percentage
        discount_dec = discount.replace('%', '.')
        boothDiscount = int(self.booth_option) * float(discount_dec)
        booth_cost = int(self.booth_option) - boothDiscount
        self.booth_cost = booth_cost
        self.save()
        return booth_cost

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
    package_type = models.CharField(max_length=100, blank=True)
    booth_id = models.IntegerField(blank=True, null=True)
    account_number = models.CharField(max_length=10, blank=True)
    booth_cost = models.CharField(max_length=100, blank=True)
    contact = models.ManyToManyField(OnSiteContacts, blank=True)



    def __str__(self):
        date_string = self.date_selection
        related_company = rself.related_sale.company_name
        return str(related_company) + " For: " + date_string + " WPG"

    def booth_cost_cal(self):
        discount = self.related_sale.discount_percentage
        discount_dec = discount.replace('%', '.')
        boothDiscount = int(self.booth_option) * float(discount_dec)
        booth_cost = int(self.booth_option) - boothDiscount
        self.booth_cost = booth_cost
        self.save()
        return booth_cost