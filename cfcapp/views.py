from django.conf import settings
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.

from cfcapp.forms import PaymentForm
from cfcapp.models import SalesFormData
from fairs.models import TorontoFair, CalgaryFair, EdmontonFair,  WinnipegFair

class IndexPageView(TemplateView):
    template_name = 'base-html.html'
    formPayment = PaymentForm()
    form_class = PaymentForm

    def get_context_data(self, **kwargs):
    
        context = super(IndexPageView, self).get_context_data(**kwargs)    
        context.update({'form': self.formPayment, 'users': User.objects.all()})
        print(self.formPayment.fields['select_cities'].choices[0])
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print(request.POST)
        if form.is_valid():
            sales_rep = request.POST.get('sales_rep', '')
            if sales_rep == '':
                sales_rep = User.objects.get(pk=1)
            else: 
                sales_rep = User.objects.get(pk=sales_rep)
            
            print(form.instance.province)    
            company_name = request.POST.get('company_name', '')
            contact_name = request.POST.get('contact_name', '')
            address = request.POST.get('address', '')
            total_spent = request.POST.get('price', '')
            if total_spent == '':
                total_spent = 0
            float(total_spent)
            discount_amount = request.POST.get('discountAmount', '')
            discount_percentage = request.POST.get('discountPercent', '')

            secondary_address = request.POST.get('secondary_address', '')
            city = request.POST.get('city', '')
           
            province = request.POST.get('province', '')

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
            Helper function that will take in a few lists, compare them and edit a related list with selections.
            Creates proper order regardless on how the list is generated on the frontend. 
            Cleans data for sales and accounting. Displays dates for reps properly
            '''
            torontoDatesArray = ['04-24-2019', '09-17-2019', '-', '-']
            torontoList = ['-', '-', '-', '-']
            calgaryDatesArray = ['03-12-2019', '06-26-2019', '10-22-2019', '-']
            calgaryList = ['-', '-', '-', '-']
            edmontonDatesArray = ['01-29-2019', '05-28-2019', '08-13-2019', '11-19-2019']
            edmontonList = ['-', '-', '-', '-']
            winnipegDatesArray = ['04-02-2019', '07-10-2019', '07-23-2019', '-']
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
            toronto_additional_booth_option_1 = request.POST.get('additional_booth_option_toronto_April 24th, 2018', '-')
            toronto_additional_booth_option_2 = request.POST.get('additional_booth_option_toronto_September 17th, 2019', '-')
            calgary_dates = request.POST.getlist('calgary_dates')
            check_incoming_fair_dates(calgary_dates, calgaryDatesArray, calgaryList)
            calgary_booth_options = request.POST.get('calgary_booth_options', '')
            calgary_options = request.POST.getlist('calgary_options')
            calgary_options_for_db = ', '.join(calgary_options)
            calgary_additional_booth_option_1 = request.POST.get('additional_booth_option_calgary_March 12th, 2019', '-')
            calgary_additional_lunch_option_1 = request.POST.get('additional_lunch_option_calgary_March 12th, 2019', '-')
            calgary_diet_request_1 = request.POST.get('diet_request_for_calgary_March 12th, 2019', '')
            calgary_additional_booth_option_2 = request.POST.get('additional_booth_option_calgary_June 26th, 2019', '-')
            calgary_additional_lunch_option_2 = request.POST.get('additional_booth_option_calgary_June 26th, 2019', '-')
            calgary_diet_request_2 = request.POST.get('diet_request_for_calgary_June 26th, 2019', '')
            calgary_additional_booth_option_3 = request.POST.get('additional_booth_option_calgary_October 22nd, 2019', '-')
            calgary_additional_lunch_option_3 = request.POST.get('additional_booth_option_calgary_October 22nd, 2019', '-')
            calgary_diet_request_3 = request.POST.get('diet_request_for_calgary_October 22nd, 2019', '')
            calgary_venue_options = request.POST.getlist('calgary_options')
            calgary_venue_options_for_db = ', '.join(calgary_venue_options)
            edmonton_dates = request.POST.getlist('edmonton_dates')
            check_incoming_fair_dates(edmonton_dates, edmontonDatesArray, edmontonList)
            edmonton_booth_options = request.POST.get('edmonton_booth_options', '')
            edmonton_additional_booth_option_1 = request.POST.get('additional_booth_option_edmonton_January 29th, 2019', '-')
            edmonton_additional_lunch_option_1 = request.POST.get('additional_lunch_option_edmonton_January 29th, 2019', '-')
            edmonton_additional_breakfast_option_1 = request.POST.get('additional_breakfast_option_edmonton_January 29th, 2019', '-')
            edmonton_diet_request_1 = request.POST.get('diet_request_for_edmonton_January 29th, 2019', '')
            edmonton_additional_booth_option_2 = request.POST.get('additional_booth_option_edmonton_May 28th, 2019', '-')
            edmonton_additional_lunch_option_2 = request.POST.get('additional_lunch_option_edmonton_May 28th, 2019', '-')
            edmonton_additional_breakfast_option_2 = request.POST.get('diet_request_for_edmonton_May 28th, 2019', '-')
            edmonton_diet_request_2 = request.POST.get('diet_request_for_edmonton_January 29th, 2019', '')
            edmonton_additional_booth_option_3 = request.POST.get('additional_booth_option_edmonton_August 13th, 2019', '-')
            edmonton_additional_lunch_option_3 = request.POST.get('additional_lunch_option_edmonton_August 13th, 2019', '-')
            edmonton_additional_breakfast_option_3 = request.POST.get('additional_breakfast_option_edmonton_August 13th, 2019', '-')
            edmonton_diet_request_3 = request.POST.get('diet_request_for_edmonton_August 13th, 2019', '')
            edmonton_additional_booth_option_4 = request.POST.get('additional_booth_option_edmonton_November 19th, 2019', '-')
            edmonton_additional_lunch_option_4 = request.POST.get('additional_lunch_option_edmonton_January 29th, 2019', '-')
            edmonton_additional_breakfast_option_4 = request.POST.get('additional_breakfast_option_edmonton_January 29th, 2019', '-')
            edmonton_diet_request_4 = request.POST.get('diet_request_for_edmonton_November 19th, 2019', '')
            edmonton_venue_options = request.POST.getlist('edmonton_options')
            edmonton_venue_options_for_db = ', '.join(edmonton_venue_options)
            
            winnipeg_dates = request.POST.getlist('winnipeg_dates')
            check_incoming_fair_dates(winnipeg_dates, winnipegDatesArray, winnipegList)
            
            winnipeg_booth_options = request.POST.get('winnipeg_booth_options', '')
            
            winnipeg_additional_booth_option_1 = request.POST.get('additional_booth_option_winnipeg_April 2nd, 2019', '-')
            winnipeg_additional_lunch_option_1 = request.POST.get('additional_lunch_option_winnipeg_April 2nd, 2019', '-')
            winnipeg_diet_request_1 = request.POST.get('diet_request_for_winnipeg_April 2nd, 2019', '')
            winnipeg_additional_booth_option_2 = request.POST.get('additional_booth_option_winnipeg_July 10th, 2019', '-')
            winnipeg_additional_lunch_option_2 = request.POST.get('additional_lunch_option_winnipeg_July 10th, 2019', '-')
            winnipeg_diet_request_2 = request.POST.get('diet_request_for_winnipeg_July 10th, 2019', '')
            winnipeg_additional_booth_option_3 = request.POST.get('additional_booth_option_winnipeg_July 23rd, 2019', '-')
            winnipeg_additional_lunch_option_3 = request.POST.get('additional_lunch_option_winnipeg_July 23rd, 2019', '-')
            winnipeg_diet_request_3 = request.POST.get('diet_request_for_winnipeg_July 23rd, 2019', '-')

            m = SalesFormData(
                sales_rep=sales_rep,
                company_name=company_name,
                contact_name=contact_name,
                total_spent=total_spent,
                discount_amount=discount_amount,
                discount_percentage=discount_percentage,
                address=address,
                secondary_address=secondary_address,
                city=city,
                province=province,
                postal_code=postal_code,
                contact_email=contact_email,
                office_phone_number=office_phone_number,
                direct_phone_number=direct_phone_number,
                facebook_link=facebook_link,
                website_link=website_link,
                twitter_link=twitter_link,
                select_cities=select_cities_for_db,
                )
            m.save()

            if 'Toronto' in select_cities:
                t_qs = TorontoFair(
                    related_sale=m,
                    toronto_dates=toronto_dates,
                    toronto_date_1=torontoList[0],
                    toronto_date_2=torontoList[1],
                    toronto_booth_options=toronto_booth_options,
                    toronto_additional_booth_option_1=toronto_additional_booth_option_1,
                    toronto_additional_booth_option_2=toronto_additional_booth_option_2
                )
                t_qs.save()
                m.toronto_booking = t_qs
                m.save()


            if 'Calgary' in select_cities:
                c_qs = CalgaryFair(
                    related_sale=m,
                    calgary_dates=calgary_dates,
                    calgary_date_1=calgaryList[0],
                    calgary_date_2=calgaryList[1],
                    calgary_date_3=calgaryList[2],
                    calgary_booth_options=calgary_booth_options,
                    calgary_additional_booth_option_2=calgary_additional_booth_option_2,
                    calgary_additional_booth_option_1=calgary_additional_booth_option_1,
                    calgary_additional_booth_option_3=calgary_additional_booth_option_3,
                    calgary_additional_lunch_option_1=calgary_additional_lunch_option_1,
                    calgary_additional_lunch_option_2=calgary_additional_lunch_option_2,
                    calgary_additional_lunch_option_3=calgary_additional_lunch_option_3,
                    calgary_diet_request_1=calgary_diet_request_1,
                    calgary_diet_request_2=calgary_diet_request_2,
                    calgary_diet_request_3=calgary_diet_request_3,
                    calgary_venue_options=calgary_venue_options_for_db
                )
                c_qs.save()
                m.calgary_booking = c_qs
                m.save()

            if 'Edmonton' in select_cities:
                e_qs = EdmontonFair(
                    related_sale=m,
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
                    edmonton_diet_request_1=edmonton_diet_request_1,
                    edmonton_diet_request_2=edmonton_diet_request_2,
                    edmonton_diet_request_3=edmonton_diet_request_3,
                    edmonton_diet_request_4=edmonton_diet_request_4
                    )
                e_qs.save()
                m.edmonton_booking = e_qs
                m.save()

            if 'Winnipeg' in select_cities:
                w_qs = WinnipegFair(
                    related_sale=m,
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
                    winnipeg_diet_request_1=winnipeg_diet_request_1,
                    winnipeg_diet_request_2=winnipeg_diet_request_2,
                    winnipeg_diet_request_3=winnipeg_diet_request_3
                )
                w_qs.save()
                m.winnipeg_booking = w_qs

            m.save()

            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})