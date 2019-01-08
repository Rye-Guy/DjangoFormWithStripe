from django.db import models
from django.contrib.auth.models import User

class SalesFormData(models.Model):

    class Meta:
        verbose_name = 'Career Fair Form'

    sales_rep = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    company_name = models.CharField(max_length=255, blank=False)
    contact_name = models.CharField(max_length=255, blank=False)
    address = models.CharField(max_length=255, blank=False)
    city_or_province = models.CharField(max_length=255, blank=False)
    postal_code = models.CharField(max_length=255, blank=False)
    contact_email = models.EmailField(blank=False)
    office_phone_number = models.CharField(max_length=88, blank=True)
    direct_phone_number = models.CharField(max_length=88, blank=True)
    facebook_link = models.URLField(max_length=255, blank=True)
    website_link = models.URLField(max_length=255, blank=True)
    twitter_link = models.URLField(max_length=255, blank=True)

    select_cities = models.CharField(max_length=255, blank=False, default='You will never see me')

    toronto_dates = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    toronto_booth_options = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    toronto_date_1 = models.CharField(max_length=400, blank=True, default='-')
    toronto_date_2 = models.CharField(max_length=400, blank=True, default='-')
    toronto_additional_booth_option_1 = models.CharField(max_length=400, default='-')
    toronto_additional_booth_option_2 = models.CharField(max_length=400, default='-')


    calgary_dates = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    calgary_booth_options = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    calgary_options = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    calgary_date_1 = models.CharField(max_length=400, blank=True, default='-')
    calgary_date_2 = models.CharField(max_length=400, blank=True, default='-')
    calgary_date_3 = models.CharField(max_length=400, blank=True, default='-')

    calgary_additional_booth_option_1 = models.CharField(max_length=400, default='-')
    calgary_additional_booth_option_2 = models.CharField(max_length=400, default='-')
    calgary_additional_booth_option_3 = models.CharField(max_length=400, default='-')
    calgary_additional_lunch_option_1 = models.CharField(max_length=400, default='-')
    calgary_additional_lunch_option_2 = models.CharField(max_length=400, default='-')
    calgary_additional_lunch_option_3 = models.CharField(max_length=400, default='-')
    calgary_diet_request = models.CharField(max_length=400, blank=True, default='-')
    calgary_venue_options = models.CharField(max_length=255, blank=False, default='-')

    edmonton_dates = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    edmonton_booth_options = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    edmonton_date_1 = models.CharField(max_length=400, blank=True, default='-')
    edmonton_date_2 = models.CharField(max_length=400, blank=True, default='-')
    edmonton_date_3 = models.CharField(max_length=400, blank=True, default='-')
    edmonton_date_4 = models.CharField(max_length=400, blank=True, default='-')
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
    edmonton_diet_request = models.CharField(max_length=400, blank=True, default='-')
    edmonton_venue_options = models.CharField(max_length=255, blank=False, default='-')

    winnipeg_dates = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    winnipeg_booth_options = models.CharField(max_length=400, blank=True, default='Value Determined By Checkbox')
    winnipeg_date_1 = models.CharField(max_length=400, blank=True, default='-')
    winnipeg_date_2 = models.CharField(max_length=400, blank=True, default='-')
    winnipeg_date_3 = models.CharField(max_length=400, blank=True, default='-')
    winnipeg_additional_booth_option_1 = models.CharField(max_length=400, default='-')
    winnipeg_additional_booth_option_2 = models.CharField(max_length=400, default='-')
    winnipeg_additional_booth_option_3 = models.CharField(max_length=400, default='-')
    winnipeg_additional_lunch_option_1 = models.CharField(max_length=400, default='-')
    winnipeg_additional_lunch_option_2 = models.CharField(max_length=400, default='-')
    winnipeg_additional_lunch_option_3 = models.CharField(max_length=400, default='-')
    winnipeg_diet_request = models.CharField(max_length=400, blank=True, default='-')