from django.db import models


# Create your models here.
CITY_CHOICES = (
    ('Toronto', 'Toronto'),
    ('Winnipeg', 'Winnipeg'),
    ('Calgary', 'Calgary'),
    ('Edmonton', 'Edmonton')
)

BOOTH_PACKAGES = (
    ('platinum', 'Platinum'),
    ('gold', 'Gold'),
    ('silver', 'Silver'),
    ('bronze', 'Bronze')
)
#
# BOOTH_OPTIONS = (
#
# )



class ShowsModel(models.Model):
    city = models.CharField(max_length=255, required=True)
    fair_dates = models.CharField(max_length=255, choices=CITY_CHOICES)


class BoothsModel(models.Model):
    associated_fair = models.ForeignKey('ShowsModel', on_delete=models.SET_NULL(None))
    booth_packages = models.CharField(max_length=255, choices=BOOTH_PACKAGES)
    additional_options = models.CharField(max_length=255, choices=BOOTH_PACKAGES)

class CustomerFormModel(models.Model):
    company_name = models.CharField(max_length=255, required=True)
    contact_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, required=True)
    city_or_province = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    contact_email = models.EmailField(required=True)
    office_phone_number = models.CharField(max_length=88)
    direct_phone_number = models.CharField(max_length=88)
    facebook_link = models.URLField(max_length=255)
    website_link = models.URLField(max_length=255)
    twitter_link = models.URLField(max_length=255)