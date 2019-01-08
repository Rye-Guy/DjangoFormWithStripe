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


            '''
            Helper function that will take in a couple of list compare them and edit a new list with related selections. Cleans data for sales and accounting.
            '''
            torontoDatesArray = ['TO APR-24-2018', 'TO SEPT-17-2019', '-', '-']
            torontoList = ['-', '-', '-', '-']

            calgaryDatesArray = ['CAL MAR-12-2019', 'CAL JUN-26-2019', 'CAL OCT-22-2019', '-']
            calgaryList = ['-', '-', '-', '-']

            edmontonDatesArray = ['EDM JAN-29-2019', 'EDM MAY-28-2019', 'EDM AUG-13-2019', 'EDM NOV-19-2019']
            edmontonList = ['-', '-', '-', '-']

            winnipegDatesArray = ['WIN JUL-10-2019', 'WIN APR-02-2019', 'WIN JUL-23-2019', '-']
            winnipegList = ['-', '-', '-', '-']

            def check_incoming_fair_dates(datesArray, dateCheckArray, listToEdit):
                for date in range(0, len(datesArray)):
                    if datesArray[date] == dateCheckArray[0]:
                        listToEdit[0] = datesArray[date]
                    if datesArray[date] == dateCheckArray[1]:
                        listToEdit[1] = datesArray[date]
                    if datesArray[date] == dateCheckArray[2]:
                        listToEdit[2] = datesArray[date]
                    if datesArray[date] == dateCheckArray[3]:
                        listToEdit[3] = datesArray[date]


            check_incoming_fair_dates(toronto_dates, torontoDatesArray, torontoList)

            toronto_booth_options = request.POST.get('toronto_booth_options', '')
            toronto_additional_booth_option_1 = request.POST.get('additional_booth_option_toronto April 24th, 2018', '-')
            toronto_additional_booth_option_2 = request.POST.get('additional_booth_option_toronto September 17th, 2019', '-')

            calgary_dates = request.POST.getlist('calgary_dates')
            check_incoming_fair_dates(calgary_dates, calgaryDatesArray, calgaryList)



            calgary_booth_options = request.POST.get('calgary_booth_options', '')
            calgary_options = request.POST.getlist('calgary_options')
            calgary_options_for_db = ', '.join(calgary_options)

            calgary_additional_booth_option_1 = request.POST.get('additional_booth_option_calgary March 12th, 2019', '-')
            calgary_additional_lunch_option_1 = request.POST.get('additional_lunch_option_calgary March 12th, 2019', '-')
            calgary_additional_booth_option_2 = request.POST.get('additional_booth_option_calgary June 26th, 2019', '-')
            calgary_additional_lunch_option_2 = request.POST.get('additional_booth_option_calgary June 26th, 2019', '-')
            calgary_additional_booth_option_3 = request.POST.get('additional_booth_option_calgary October 22nd, 2019', '-')
            calgary_additional_lunch_option_3 = request.POST.get('additional_booth_option_calgary October 22nd, 2019', '-')

            calgary_venue_options = request.POST.getlist('calgary_options')
            calgary_venue_options_for_db = ', '.join(calgary_venue_options)

            calgary_diet_request = request.POST.get('calgary_diet_request', '-')


            edmonton_dates = request.POST.getlist('edmonton_dates')
            check_incoming_fair_dates(edmonton_dates, edmontonDatesArray, edmontonList)
            edmonton_booth_options = request.POST.get('edmonton_booth_options', '')


            edmonton_additional_booth_option_1 = request.POST.get('additional_booth_option_edmonton January 29th, 2019', '-')
            edmonton_additional_lunch_option_1 = request.POST.get('additional_lunch_option_edmonton January 29th, 2019', '-')
            edmonton_additional_breakfast_option_1 = request.POST.get('additional_breakfast_option_edmonton January 29th, 2019', '-')

            edmonton_additional_booth_option_2 = request.POST.get('additional_booth_option_edmonton May 28th, 2019', '-')
            edmonton_additional_lunch_option_2 = request.POST.get('additional_lunch_option_edmonton May 28th, 2019', '-')
            edmonton_additional_breakfast_option_2 = request.POST.get('additional_breakfast_option_edmonton May 28th, 2019', '-')

            edmonton_additional_booth_option_3 = request.POST.get('additional_booth_option_edmonton August 13th, 2019', '-')
            edmonton_additional_lunch_option_3 = request.POST.get('additional_lunch_option_edmonton August 13th, 2019', '-')
            edmonton_additional_breakfast_option_3 = request.POST.get('additional_breakfast_option_edmonton August 13th, 2019', '-')

            edmonton_additional_booth_option_4 = request.POST.get('additional_booth_option_edmonton November 19th, 2019', '-')
            edmonton_additional_lunch_option_4 = request.POST.get('additional_lunch_option_edmonton January 29th, 2019', '-')
            edmonton_additional_breakfast_option_4 = request.POST.get('additional_breakfast_option_edmonton January 29th, 2019', '-')

            edmonton_venue_options = request.POST.getlist('edmonton_options')
            edmonton_venue_options_for_db = ', '.join(edmonton_venue_options)

            edmonton_diet_request = request.POST.get('edmonton_diet_request', '-')


            winnipeg_dates = request.POST.getlist('winnipeg_dates')
            check_incoming_fair_dates(winnipeg_dates, winnipegDatesArray, winnipegList)

            winnipeg_booth_options = request.POST.get('winnipeg_booth_options', '')
            winnipeg_additional_booth_option_1 = request.POST.get('additional_booth_option_winnipeg July 10th, 2019', '-')
            winnipeg_additional_lunch_option_1 = request.POST.get('additional_lunch_option_winnipeg July 10th, 2019', '-')
            winnipeg_additional_booth_option_2 = request.POST.get('additional_booth_option_winnipeg April 2nd, 2019', '-')
            winnipeg_additional_lunch_option_2 = request.POST.get('additional_lunch_option_winnipeg April 2nd, 2019', '-')
            winnipeg_additional_booth_option_3 = request.POST.get('additional_booth_option_winnipeg July 23rd, 2019', '-')
            winnipeg_additional_lunch_option_3 = request.POST.get('additional_lunch_option_winnipeg July 23rd, 2019', '-')
            winnipeg_diet_request = request.POST.get('winnipeg_diet_request', '-')

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
                toronto_date_1=torontoList[0],
                toronto_date_2=torontoList[1],
                toronto_booth_options=toronto_booth_options,
                toronto_additional_booth_option_1=toronto_additional_booth_option_1,
                toronto_additional_booth_option_2=toronto_additional_booth_option_2,


                calgary_dates=calgary_dates,
                calgary_date_1=calgaryList[0],
                calgary_date_2=calgaryList[1],
                calgary_date_3=calgaryList[2],
                calgary_booth_options=calgary_booth_options,
                calgary_additional_booth_option_1=calgary_additional_booth_option_1,
                calgary_additional_booth_option_2=calgary_additional_booth_option_2,
                calgary_additional_booth_option_3=calgary_additional_booth_option_3,
                calgary_additional_lunch_option_1=calgary_additional_lunch_option_1,
                calgary_additional_lunch_option_2=calgary_additional_lunch_option_2,
                calgary_additional_lunch_option_3=calgary_additional_lunch_option_3,
                calgary_venue_options=calgary_venue_options_for_db,
                calgary_diet_request=calgary_diet_request,

                edmonton_dates=edmonton_dates,
                edmonton_date_1=edmontonList[0],
                edmonton_date_2=edmontonList[1],
                edmonton_date_3=edmontonList[2],
                edmonton_date_4=edmontonList[3],
                edmonton_booth_options=edmonton_booth_options,
                edmonton_additional_booth_option_1=edmonton_additional_booth_option_1,
                edmonton_additional_booth_option_2=edmonton_additional_booth_option_2,
                edmonton_additional_booth_option_3=edmonton_additional_booth_option_3,
                edmonton_additional_booth_option_4=edmonton_additional_booth_option_4,
                edmonton_additional_lunch_option_1=edmonton_additional_lunch_option_1,
                edmonton_additional_lunch_option_2=edmonton_additional_lunch_option_2,
                edmonton_additional_lunch_option_3=edmonton_additional_lunch_option_3,
                edmonton_additional_lunch_option_4=edmonton_additional_lunch_option_4,
                edmonton_additional_breakfast_option_1=edmonton_additional_breakfast_option_1,
                edmonton_additional_breakfast_option_2=edmonton_additional_breakfast_option_2,
                edmonton_additional_breakfast_option_3=edmonton_additional_breakfast_option_3,
                edmonton_additional_breakfast_option_4=edmonton_additional_breakfast_option_4,
                edmonton_venue_options=edmonton_venue_options_for_db,
                edmonton_diet_request=edmonton_diet_request,

                winnipeg_dates=winnipeg_dates,
                winnipeg_date_1=winnipegList[0],
                winnipeg_date_2=winnipegList[1],
                winnipeg_date_3=winnipegList[2],
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

