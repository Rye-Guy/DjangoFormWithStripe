from django.conf import settings
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
# Create your views here.

from form.forms import PaymentForm
from form.models import SalesFormData


import stripe

class IndexPageView(TemplateView):
    template_name = 'base-html.html'
    formPayment = PaymentForm()
    form_class = PaymentForm


    stripeApiKey = settings.STRIPE_SECRET_KEY

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        context.update({'form': self.formPayment})
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print(request.POST)
        if form.is_valid():

            company_name = request.POST.get('company_name', '')
            contact_name = request.POST.get('contact_name', '')
            address = request.POST.get('address', '')
            city_or_province = request.POST.get('city_or_province', '')
            postal_code = request.POST.get('postal_code', '')
            contact_email = request.POST.get('contact_email', '')
            office_phone_number = request.POST.get('office_phone_number', '')
            direct_phone_number = request.POST.get('direct_phone_number', '')
            facebook_link = request.POST.get('facebook_link', '')
            website_link = request.POST.get('website_link', '')
            twitter_link = request.POST.get('twitter_link', '')

            select_cities = request.POST.getlist('select_cities')
            select_cities_for_db = ', '.join(select_cities)

            toronto_dates = request.POST.getlist('toronto_dates')
            toronto_booth_options = request.POST.get('toronto_booth_options', '')
            toronto_additional_booth_option_1 = request.POST.get('additional_booth_option_toronto April 24th, 2018', 'N/A')
            toronto_additional_booth_option_2 = request.POST.get('additional_booth_option_toronto September 17th, 2019', 'N/A')

            calgary_dates = request.POST.getlist('calgary_dates')
            calgary_booth_options = request.POST.get('calgary_booth_options', '')
            calgary_options = request.POST.getlist('calgary_options')
            calgary_additional_booth_option_1 = request.POST.get('additional_booth_option_calgary March 12th, 2019', 'N/A')
            calgary_additional_booth_option_2 = request.POST.get('additional_booth_option_calgary June 26th, 2019', 'N/A')
            calgary_additional_booth_option_3 = request.POST.get('additional_booth_option_calgary October 22nd, 2019', 'N/A')

            edmonton_dates = request.POST.getlist('edmonton_dates')
            edmonton_booth_options = request.POST.get('edmonton_booth_options', '')
            edmonton_options = request.POST.getlist('edmonton_options')
            edmonton_additional_booth_option_1 = request.POST.get('additional_booth_option_edmonton January 29th, 2019', 'N/A')
            edmonton_additional_booth_option_2 = request.POST.get('additional_booth_option_edmonton May 28th, 2019', 'N/A')
            edmonton_additional_booth_option_3 = request.POST.get('additional_booth_option_edmonton August 13th, 2019', 'N/A')
            edmonton_additional_booth_option_4 = request.POST.get('additional_booth_option_edmonton November 19th, 2019', 'N/A')

            winnipeg_dates = request.POST.get('winnipeg_date', '')
            winnipeg_booth_options = request.POST.get('winnipeg_booth_options', '')
            winnipeg_additional_booth_option_1 = request.POST.get('additional_booth_option_winnipeg July 10th, 2019', 'N/A')
            winnipeg_additional_lunch_option_1 = request.POST.get('additional_lunch_option_winnipeg July 10th, 2019', 'N/A')
            winnipeg_additional_booth_option_2 = request.POST.get('additional_booth_option_winnipeg April 2nd, 2019', 'N/A')
            winnipeg_additional_lunch_option_2 = request.POST.get('additional_lunch_option_winnipeg April 2nd, 2019', 'N/A')
            winnipeg_additional_booth_option_3 = request.POST.get('additional_booth_option_winnipeg July 23rd, 2019', 'N/A')
            winnipeg_additional_lunch_option_3 = request.POST.get('additional_lunch_option_winnipeg July 23rd, 2019', 'N/A')
            winnipeg_diet_request = request.POST.get('winnipeg_diet_request', 'N/A')

            m = SalesFormData(
                company_name=company_name,
                contact_name=contact_name,
                address=address,
                city_or_province=city_or_province,
                postal_code=postal_code,
                contact_email=contact_email,
                office_phone_number=office_phone_number,
                direct_phone_number=direct_phone_number,
                facebook_link=facebook_link,
                website_link=website_link,
                twitter_link=twitter_link,

                select_cities=select_cities_for_db,

                toronto_dates=toronto_dates,
                toronto_booth_options=toronto_booth_options,
                toronto_additional_booth_option_1=toronto_additional_booth_option_1,
                toronto_additional_booth_option_2=toronto_additional_booth_option_2,

                calgary_dates=calgary_dates,
                calgary_booth_options=calgary_booth_options,
                calgary_options=calgary_options,
                calgary_additional_booth_option_1=calgary_additional_booth_option_1,
                calgary_additional_booth_option_2=calgary_additional_booth_option_2,
                calgary_additional_booth_option_3=calgary_additional_booth_option_3,

                edmonton_dates=edmonton_dates,
                edmonton_booth_options=edmonton_booth_options,
                edmonton_options=edmonton_options,
                edmonton_additional_booth_option_1=edmonton_additional_booth_option_1,
                edmonton_additional_booth_option_2=edmonton_additional_booth_option_2,
                edmonton_additional_booth_option_3=edmonton_additional_booth_option_3,
                edmonton_additional_booth_option_4=edmonton_additional_booth_option_4,

                winnipeg_dates=winnipeg_dates,
                winnipeg_booth_options=winnipeg_booth_options,
                winnipeg_additional_booth_option_1=winnipeg_additional_booth_option_1,
                winnipeg_additional_booth_option_2=winnipeg_additional_booth_option_2,
                winnipeg_additional_booth_option_3=winnipeg_additional_booth_option_3,
                winnipeg_additional_lunch_option_1=winnipeg_additional_lunch_option_1,
                winnipeg_additional_lunch_option_2=winnipeg_additional_lunch_option_2,
                winnipeg_additional_lunch_option_3=winnipeg_additional_lunch_option_3,
                winnipeg_diet_request=winnipeg_diet_request
                )
            m.save()


            # stripe.Charge.create(
            #     amount=price,
            #     currency='cad',
            #     description='Django stripe charge',
            #     source=request.POST['stripeToken']
            # )
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})

