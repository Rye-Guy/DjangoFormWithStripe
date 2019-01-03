from django.db import models


class CustomerModelForm(models.Model):
    company_name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city_or_province = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    contact_email = models.EmailField()
    office_phone_number = models.CharField(max_length=88, blank=True)
    direct_phone_number = models.CharField(max_length=88, blank=True)
    facebook_link = models.URLField(max_length=255, blank=True)
    website_link = models.URLField(max_length=255, blank=True)
    twitter_link = models.URLField(max_length=255, blank=True)


class SalesFormData(models.Model):

    class Meta:
        verbose_name = 'Career Fair Form'

    company_name = models.CharField(max_length=255, blank=False)
    contact_name = models.CharField(max_length=255, blank=False)
    address = models.CharField(max_length=255, blank=False, default='Not Provided')
    city_or_province = models.CharField(max_length=255, blank=False, default='Not Provided')
    postal_code = models.CharField(max_length=255, blank=False, default='Not Provided')
    contact_email = models.EmailField(blank=False, default='Not Provided')
    office_phone_number = models.CharField(max_length=88, blank=True)
    direct_phone_number = models.CharField(max_length=88, blank=True)
    facebook_link = models.URLField(max_length=255, blank=True)
    website_link = models.URLField(max_length=255, blank=True)
    twitter_link = models.URLField(max_length=255, blank=True)

    select_cities = models.CharField(max_length=255, blank=False, default='You will never see me')

    toronto_dates = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    toronto_booth_options = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    toronto_additional_booth_option_1 = models.CharField(max_length=400, default='N/A')
    toronto_additional_booth_option_2 = models.CharField(max_length=400, default='N/A')

    calgary_dates = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    calgary_booth_options = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    calgary_options = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    calgary_additional_booth_option_1 = models.CharField(max_length=400, default='N/A')
    calgary_additional_booth_option_2 = models.CharField(max_length=400, default='N/A')
    calgary_additional_booth_option_3 = models.CharField(max_length=400, default='N/A')

    edmonton_dates = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    edmonton_booth_options = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    edmonton_options = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    edmonton_additional_booth_option_1 = models.CharField(max_length=400, default='N/A')
    edmonton_additional_booth_option_2 = models.CharField(max_length=400, default='N/A')
    edmonton_additional_booth_option_3 = models.CharField(max_length=400, default='N/A')
    edmonton_additional_booth_option_4 = models.CharField(max_length=400, default='N/A')

    winnipeg_dates = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    winnipeg_booth_options = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    winnipeg_additional_booth_option_1 = models.CharField(max_length=400, default='N/A')
    winnipeg_additional_booth_option_2 = models.CharField(max_length=400, default='N/A')
    winnipeg_additional_booth_option_3 = models.CharField(max_length=400, default='N/A')


