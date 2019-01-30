from django.db import models
from django.contrib.auth.models import User
class SalesFormData(models.Model):

    class Meta:
        verbose_name = 'Career Fair Form'

    def __unicode__(self):
        return self.id

    sales_rep = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=False)
    contact_name = models.CharField(max_length=255, blank=False)
    total_spent = models.DecimalField(max_digits=7, decimal_places=2, blank=False)
    discount_amount = models.CharField(max_length=50, blank=True, default=0) 
    discount_percentage = models.CharField(max_length=10, blank=True, default='Not Provided')
    grand_total = models.DecimalField(max_digits=7, decimal_places=2, blank=False, default=0)
    address = models.CharField(max_length=255, blank=False)
    secondary_address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=False)
    province = models.CharField(max_length=255, blank=False)
    postal_code = models.CharField(max_length=255, blank=False)
    contact_email = models.EmailField(blank=False)
    office_phone_number = models.CharField(max_length=88, blank=True)
    direct_phone_number = models.CharField(max_length=88, blank=True)
    facebook_link = models.URLField(max_length=255, blank=True)
    website_link = models.URLField(max_length=255, blank=True)
    twitter_link = models.URLField(max_length=255, blank=True)
    select_cities = models.CharField(max_length=255, blank=False, default='You will never see me')
    toronto_booking = models.ForeignKey('fairs.TorontoFair', on_delete=models.SET_NULL, null=True, blank=True)
    edmonton_booking = models.ForeignKey('fairs.EdmontonFair', on_delete=models.SET_NULL, null=True, blank=True)
    calgary_booking = models.ForeignKey('fairs.CalgaryFair', on_delete=models.SET_NULL, null=True, blank=True)
    winnipeg_booking = models.ForeignKey('fairs.WinnipegFair', on_delete=models.SET_NULL, null=True, blank=True)