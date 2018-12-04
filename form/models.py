from django.db import models


# Create your models here.
# CITY_CHOICES = (
#     ('Toronto', 'Toronto'),
#     ('Winnipeg', 'Winnipeg'),
#     ('Calgary', 'Calgary'),
#     ('Edmonton', 'Edmonton')
# )
#
# FAIR_DATES = (
#     ('jun1', 'June 1st'),
#     ('july2', 'July 2nd'),
#     ('august3', 'August 3rd'),
#     ('september4', 'September 4th')
# )
#
# BOOTH_PACKAGES = (
#     ('platinum', 'Platinum'),
#     ('gold', 'Gold'),
#     ('silver', 'Silver'),
#     ('bronze', 'Bronze')
# )
#
# BOOTH_OPTIONS = (
#
# )


#
# class ShowsModel(models.Model):
#     city = models.CharField(max_length=255, choices=CITY_CHOICES)
#     fair_dates = models.CharField(max_length=255, choices=FAIR_DATES)
#
#
# class BoothsModel(models.Model):
#     associated_fair = models.ForeignKey('ShowsModel', on_delete=models.SET_NULL, null=True)
#     booth_packages = models.CharField(max_length=255, choices=BOOTH_PACKAGES)
#     additional_options = models.CharField(max_length=255, choices=BOOTH_PACKAGES)
#
# class CustomerFormModel(models.Model):
#     company_name = models.CharField(max_length=255)
#     contact_name = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     city_or_province = models.CharField(max_length=255)
#     postal_code = models.CharField(max_length=255)
#     contact_email = models.EmailField()
#     office_phone_number = models.CharField(max_length=88)
#     direct_phone_number = models.CharField(max_length=88)
#     facebook_link = models.URLField(max_length=255)
#     website_link = models.URLField(max_length=255)
#     twitter_link = models.URLField(max_length=255)