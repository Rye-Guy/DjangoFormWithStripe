from django.db import models
from django.conf import settings

import stripe

class CustomerModelForm(models.Model):
    company_name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city_or_province = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    contact_email = models.EmailField()
    office_phone_number = models.CharField(max_length=88)
    direct_phone_number = models.CharField(max_length=88)
    facebook_link = models.URLField(max_length=255)
    website_link = models.URLField(max_length=255)
    twitter_link = models.URLField(max_length=255)
