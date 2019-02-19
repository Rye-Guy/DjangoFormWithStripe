from django.db import models
from django.contrib.auth.models import User

from decimal import *

class SalesFormData(models.Model):

    class Meta:
        verbose_name = 'Career Fair Form'

    def __str__(self):
        part1 = self.company_name
        part2 = self.id
        reable_str = part1 + ' id:' + str(part2)
        return reable_str



    def save(self, *args, **kwargs):

        def calculate_individual_fair_cost(obj, percentage_dec):
            mydiff = int(obj.booth_option) * percentage_dec
            boothCost = int(obj.booth_option) - mydiff
            obj.booth_cost = boothCost
            newFairTotal = boothCost + float(obj.fair_total_spent) - obj.booth_cost
            print(obj.additional_booth_option)
            print(obj.related_class())
            obj.save()
            return newFairTotal

        discount_amount = self.discount_amount
        discount_percentage = self.discount_percentage
        percent_to_remove = (discount_percentage.split('%'))
        percentage_int = int(float(percent_to_remove[1]))
        percentage_dec = float('.' + str(percentage_int))


        total_spent = self.total_spent
        toronto_booking = self.toronto_booking
        print('|------------------------------------------------------------------|')
        print('toronto bookings:')
        print(self.toronto_booking.all())
        toronto_qs = self.toronto_booking.all()
        toronto_cost = 0
        for obj in toronto_qs:


            print(calculate_individual_fair_cost(obj, percentage_dec))
            toronto_cost += calculate_individual_fair_cost(obj, percentage_dec)


        print('|------------------------------------------------------------------|')
        print('calgary bookings:')

        calgary_qs = self.calgary_booking.all()
        calgary_cost = 0

        for obj in calgary_qs:

            print(calculate_individual_fair_cost(obj, percentage_dec))
            calgary_cost += calculate_individual_fair_cost(obj, percentage_dec)

        print('|------------------------------------------------------------------|')

        print('edmonton bookings:')

        edmonton_qs = self.edmonton_booking.all()
        edmonton_cost = 0

        for obj in edmonton_qs:


            print(calculate_individual_fair_cost(obj, percentage_dec))
            edmonton_cost += calculate_individual_fair_cost(obj, percentage_dec)


        print('|------------------------------------------------------------------|')
        print('winnipeg bookings:')

        winnipeg_qs = self.winnipeg_booking.all()
        winnipeg_cost = 0

        for obj in winnipeg_qs:

            print(calculate_individual_fair_cost(obj, percentage_dec))
            winnipeg_cost += calculate_individual_fair_cost(obj, percentage_dec)

        print('|------------------------------------------------------------------|')

        print('Working Numbers:')
        print(discount_amount, discount_percentage, total_spent, self.subtotal)
        print(toronto_cost, calgary_cost, edmonton_cost, winnipeg_cost)
        self.subtotal = toronto_cost + calgary_cost + edmonton_cost + winnipeg_cost
        updated_subtotal = self.subtotal
        self.discount_amount = updated_subtotal * percentage_dec

        print('|------------------------------------------------------------------|')
        super(SalesFormData, self).save(*args, **kwargs)


    sales_rep = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=False)
    contact_name = models.CharField(max_length=255, blank=False)
    total_spent = models.DecimalField(max_digits=7, decimal_places=2, blank=False)
    discount_amount = models.CharField(max_length=50, blank=True, default=0) 
    discount_percentage = models.CharField(max_length=50, blank=True, default='Not Provided')
    subtotal = models.DecimalField(max_digits=7, decimal_places=2, blank=False, default=0.00)
    address = models.CharField(max_length=255, blank=False)
    secondary_address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=False)
    province = models.CharField(max_length=255, blank=False)
    industry = models.CharField(max_length=255, blank=False, default='Not Selected')
    postal_code = models.CharField(max_length=255, blank=False)
    contact_email = models.EmailField(blank=False)
    office_phone_number = models.CharField(max_length=88, blank=True)
    direct_phone_number = models.CharField(max_length=88, blank=True)
    facebook_link = models.URLField(max_length=255, blank=True)
    website_link = models.URLField(max_length=255, blank=True)
    instagram_link = models.URLField(max_length=255, blank=True)
    twitter_link = models.URLField(max_length=255, blank=True)
    select_cities = models.CharField(max_length=255, blank=False, default='You will never see me')
    toronto_booking = models.ManyToManyField('fairs.TorontoFair', blank=True)
    edmonton_booking = models.ManyToManyField('fairs.EdmontonFair', blank=True)
    calgary_booking = models.ManyToManyField('fairs.CalgaryFair', blank=True)
    winnipeg_booking = models.ManyToManyField('fairs.WinnipegFair', blank=True)


