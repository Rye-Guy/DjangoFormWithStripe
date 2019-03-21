from django.conf import settings
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.
from cfcapp.forms import PaymentForm
from cfcapp.models import SalesFormData
from fairs.models import TorontoFair, CalgaryFair, EdmontonFair,  WinnipegFair

class SuccessPage(TemplateView):
    template_name = 'success.html'

class IndexPageView(TemplateView):
    template_name = 'main-form.html'
    formPayment = PaymentForm()
    form_class = PaymentForm

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)    
        context.update({'form': self.formPayment, 'users': User.objects.all()})
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        ###print(request.POST)###

        if form.is_valid():
            sales_rep = request.POST.get('sales_rep', '')
            try:
                sales_rep = User.objects.get(pk=sales_rep)
            except ValueError:
                sales_rep = User.objects.get(username='admin')

            company_name = request.POST.get('company_name', '')
            contact_name = request.POST.get('contact_name', '')
            address = request.POST.get('address', '')
            total_spent = request.POST.get('price', '')
            if total_spent == '':
                total_spent = 0
            elif '$' in total_spent:
                total_spent = total_spent.replace('$', '')
            float(total_spent)

            subtotal = request.POST.get('subtotalInput', 0.00)


            discount_amount = request.POST.get('discountAmount', '')

            discount_percentage = request.POST.get('discountPercent', '')
            secondary_address = request.POST.get('secondary_address', '')
            city = request.POST.get('city', '')

            province = request.POST.get('province', '')
            industry = request.POST.get('industry', '')

            postal_code = request.POST.get('postal_code', '')
            contact_email = request.POST.get('contact_email', '')
            office_phone_number = request.POST.get('office_phone_number', '')
            direct_phone_number = request.POST.get('direct_phone_number', '')
            facebook_link = request.POST.get('facebook_link', '')
            website_link = request.POST.get('website_link', '')
            instagram_link = request.POST.get('twitter_link', '')
            twitter_link = request.POST.get('twitter_link', '')
            select_cities = request.POST.getlist('select_cities')
            select_cities_for_db = ', '.join(select_cities)
            toronto_dates = request.POST.getlist('toronto_dates')

            """
            Something that takes the current booth option value and returns a package title
            """
            def select_booth_package(booth_option):
                if booth_option == '1495':
                    return "Bronze"
                elif booth_option == '1995':
                    return "Silver"
                elif booth_option == '2495':
                    return "Gold"
                elif booth_option == '2995':
                    return "Platinum"

            '''
            worked in booleans to be sent to database as True or False if the checkbox is 'on'
            '''
            def check_boolean(data):
                if data == 'on':
                    return True
                return False


            def fix_lunch_issue(lunch_option):
                print(lunch_option)
                if lunch_option == '-':
                    return lunch_option
                auto_add_2_lunches = int(lunch_option) + 2
                return auto_add_2_lunches


            '''
            Helper function that will take in a few lists, compare them and edit a related list with selections.
            Creates proper order regardless on how the list is generated on the frontend. 
            Cleans data for sales and accounting. Displays dates for reps properly
            '''

            torontoDatesArray = ['04-24-2019', '09-17-2019', '-', '-']
            torontoList = ['-', '-', '-', '-']
            calgaryDatesArray = ['03-12-2019', '06-25-2019', '10-23-2019', '-']
            calgaryList = ['-', '-', '-', '-']
            edmontonDatesArray = ['01-29-2019', '05-28-2019', '08-13-2019', '11-19-2019']
            edmontonList = ['-', '-', '-', '-']
            winnipegDatesArray = ['04-02-2019', '07-23-2019', '-', '-']
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
            toronto_booth_option_1 = request.POST.get('booth_option_toronto_April 24th, 2019', '')
            toronto_booth_option_2 = request.POST.get('booth_option_toronto_September 17th, 2019', '')
            toronto_additional_booth_option_1 = request.POST.get('additional_booth_option_toronto_April 24th, 2019', '-')
            toronto_additional_booth_option_2 = request.POST.get('additional_booth_option_toronto_September 17th, 2019', '-')
            calgary_dates = request.POST.getlist('calgary_dates')
            check_incoming_fair_dates(calgary_dates, calgaryDatesArray, calgaryList)
            calgary_booth_options = request.POST.get('calgary_booth_options', '')
            calgary_options = request.POST.getlist('calgary_options')
            calgary_options_for_db = ', '.join(calgary_options)
            calgary_booth_option_1 = request.POST.get('booth_option_calgary_March 12th, 2019', '')
            calgary_booth_option_2 = request.POST.get('booth_option_calgary_June 25th, 2019', '')
            calgary_booth_option_3 = request.POST.get('booth_option_calgary_October 23rd, 2019', '')
            calgary_additional_booth_option_1 = request.POST.get('additional_booth_option_calgary_March 12th, 2019', '-')
            calgary_additional_lunch_option_1 = request.POST.get('additional_lunch_option_calgary_March 12th, 2019', '-')
            calgary_diet_request_1 = request.POST.get('diet_request_for_calgary_March 12th, 2019', '')
            calgary_additional_booth_option_2 = request.POST.get('additional_booth_option_calgary_June 25th, 2019', '-')
            calgary_additional_lunch_option_2 = request.POST.get('additional_booth_option_calgary_June 25th, 2019', '-')
            calgary_diet_request_2 = request.POST.get('diet_request_for_calgary_June 25th, 2019', '')
            calgary_additional_booth_option_3 = request.POST.get('additional_booth_option_calgary_October 23rd, 2019', '-')
            calgary_additional_lunch_option_3 = request.POST.get('additional_booth_option_calgary_October 23rd, 2019', '-')
            calgary_diet_request_3 = request.POST.get('diet_request_for_calgary_October 23rd, 2019', '')
            calgary_venue_options = request.POST.getlist('calgary_options')
            calgary_venue_options_for_db = ', '.join(calgary_venue_options)
            edmonton_dates = request.POST.getlist('edmonton_dates')
            check_incoming_fair_dates(edmonton_dates, edmontonDatesArray, edmontonList)
            edmonton_booth_option_1 = request.POST.get('booth_option_edmonton_January 29th, 2019', '')
            edmonton_booth_option_2 = request.POST.get('booth_option_edmonton_May 28th, 2019', '')
            edmonton_booth_option_3 = request.POST.get('booth_option_edmonton_August 13th, 2019', '')
            edmonton_booth_option_4 = request.POST.get('booth_option_edmonton_November 19th, 2019', '')
            edmonton_additional_booth_option_1 = request.POST.get('additional_booth_option_edmonton_January 29th, 2019', '-')
            edmonton_additional_lunch_option_1 = request.POST.get('additional_lunch_option_edmonton_January 29th, 2019', '-')
            edmonton_diet_request_1 = request.POST.get('diet_request_for_edmonton_January 29th, 2019', '')
            edmonton_additional_booth_option_2 = request.POST.get('additional_booth_option_edmonton_May 28th, 2019', '-')
            edmonton_additional_lunch_option_2 = request.POST.get('additional_lunch_option_edmonton_May 28th, 2019', '-')
            edmonton_diet_request_2 = request.POST.get('diet_request_for_edmonton_January 29th, 2019', '')
            edmonton_additional_booth_option_3 = request.POST.get('additional_booth_option_edmonton_August 13th, 2019', '-')
            edmonton_additional_lunch_option_3 = request.POST.get('additional_lunch_option_edmonton_August 13th, 2019', '-')
            edmonton_diet_request_3 = request.POST.get('diet_request_for_edmonton_August 13th, 2019', '')
            edmonton_additional_booth_option_4 = request.POST.get('additional_booth_option_edmonton_November 19th, 2019', '-')
            edmonton_additional_lunch_option_4 = request.POST.get('additional_lunch_option_edmonton_November 19th, 2019', '-')
            edmonton_diet_request_4 = request.POST.get('diet_request_for_edmonton_November 19th, 2019', '')
            edmonton_options = request.POST.getlist('edmonton_options')
            winnipeg_dates = request.POST.getlist('winnipeg_dates')
            check_incoming_fair_dates(winnipeg_dates, winnipegDatesArray, winnipegList)
            winnipeg_booth_option_1 = request.POST.get('booth_option_winnipeg_April 2nd, 2019', '')
            winnipeg_booth_option_2 = request.POST.get('booth_option_winnipeg_July 23rd, 2019', '')
            winnipeg_additional_booth_option_1 = request.POST.get('additional_booth_option_winnipeg_April 2nd, 2019', '-')
            winnipeg_additional_lunch_option_1 = request.POST.get('additional_lunch_option_winnipeg_April 2nd, 2019', '-')
            winnipeg_diet_request_1 = request.POST.get('diet_request_for_winnipeg_April 2nd, 2019', '')
            winnipeg_additional_booth_option_2 = request.POST.get('additional_booth_option_winnipeg_July 23rd, 2019', '-')
            winnipeg_additional_lunch_option_2 = request.POST.get('additional_lunch_option_winnipeg_July 23rd, 2019', '-')
            winnipeg_diet_request_2 = request.POST.get('diet_request_for_winnipeg_July 23rd, 2019', '-')
            total_toronto_fair_cost_1 = request.POST.get('total_cost_for_toronto_April 24th, 2019', '')
            total_toronto_fair_cost_2 = request.POST.get('total_cost_for_toronto_September 17th, 2019', '')
            extra_notes_toronto_fair_1 = request.POST.get('extra_notes_for_toronto_April 24th, 2019', '')
            extra_notes_toronto_fair_2 = request.POST.get('extra_notes_for_toronto_September 17th, 2019', '')
            total_winnipeg_fair_cost_1 = request.POST.get('total_cost_for_winnipeg_April 2nd, 2019', '')
            total_winnipeg_fair_cost_2 = request.POST.get('total_cost_for_winnipeg_July 23rd, 2019', '')
            extra_notes_winnipeg_fair_1 = request.POST.get('extra_notes_for_winnipeg_April 2nd, 2019', '')
            extra_notes_winnipeg_fair_2 = request.POST.get('extra_notes_for_winnipeg_July 23rd, 2019', '')
            total_calgary_fair_cost_1 = request.POST.get('total_cost_for_calgary_March 12th, 2019', '')
            total_calgary_fair_cost_2 = request.POST.get('total_cost_for_calgary_June 25th, 2019', '')
            total_calgary_fair_cost_3 = request.POST.get('total_cost_for_calgary_October 23rd, 2019', '')
            extra_notes_calgary_fair_1 = request.POST.get('extra_notes_for_calgary_March 12th, 2019', '')
            extra_notes_calgary_fair_2 = request.POST.get('extra_notes_for_calgary_June 25th, 2019', '')
            extra_notes_calgary_fair_3 = request.POST.get('extra_notes_for_calgary_October 23rd, 2019', '')
            electricty_option_calgary_1 = request.POST.get('electricity_option_calgary_March 12th, 2019', False)
            electricty_option_calgary_2 = request.POST.get('electricity_option_calgary_June 25th, 2019', False)
            electricty_option_calgary_3 = request.POST.get('electricity_option_calgary_October 23rd, 2019', False)

            total_edmonton_fair_cost_1 = request.POST.get('total_cost_for_edmonton_January 29th, 2019', '')
            total_edmonton_fair_cost_2 = request.POST.get('total_cost_for_edmonton_May 28th, 2019', '')
            total_edmonton_fair_cost_3 = request.POST.get('total_cost_for_edmonton_August 13th, 2019', '')
            total_edmonton_fair_cost_4 = request.POST.get('total_cost_for_edmonton_November 19th, 2019', '')
            extra_notes_edmonton_fair_1 = request.POST.get('extra_notes_for_edmonton_January 29th, 2019', '')
            extra_notes_edmonton_fair_2 = request.POST.get('extra_notes_for_edmonton_May 28th, 2019', '')
            extra_notes_edmonton_fair_3 = request.POST.get('extra_notes_for_edmonton_August 13th, 2019', '')
            extra_notes_edmonton_fair_4 = request.POST.get('extra_notes_for_edmonton_November 19th, 2019', '')

            wifi_option_calgary_fair_1 = request.POST.get('wifi_per_device_for_calgary_March 12th, 2019', '')
            wifi_option_calgary_fair_2 = request.POST.get('wifi_per_device_for_calgary_June 25th, 2019', '')
            wifi_option_calgary_fair_3 = request.POST.get('wifi_per_device_for_calgary_October 23rd, 2019', '')

            wifi_option_edmonton_fair_1 = request.POST.get('wifi_per_device_for_edmonton_January 29th, 2019', '')
            wifi_option_edmonton_fair_2 = request.POST.get('wifi_per_device_for_edmonton_May 28th, 2019', '')
            wifi_option_edmonton_fair_3 = request.POST.get('wifi_per_device_for_edmonton_August 13th, 2019', '')
            wifi_option_edmonton_fair_4 = request.POST.get('wifi_per_device_for_edmonton_November 19th, 2019', '')

            m = SalesFormData(
                sales_rep=sales_rep,
                company_name=company_name,
                contact_name=contact_name,
                total_spent=total_spent,
                subtotal=subtotal,
                discount_amount=discount_amount,
                discount_percentage=discount_percentage,
                address=address,
                secondary_address=secondary_address,
                city=city,
                province=province,
                industry=industry,
                postal_code=postal_code,
                contact_email=contact_email,
                office_phone_number=office_phone_number,
                direct_phone_number=direct_phone_number,
                facebook_link=facebook_link,
                website_link=website_link,
                instagram_link=instagram_link,
                twitter_link=twitter_link,
                select_cities=select_cities_for_db,
                )
            m.save()


            if 'Toronto' in select_cities:
                for index in range(0, len(torontoList)):
                    if torontoList[index] == '-':
                        print('Date Selection is "-" so fair is not in use.')
                        pass

                    elif torontoList[index] != '-':
                        t_qs = TorontoFair(
                            related_sale=m,
                            date_selection=torontoList[index],
                        )
                        if index == 0:
                            t_qs.booth_option = toronto_booth_option_1
                            t_qs.additional_booth_option = toronto_additional_booth_option_1
                            t_qs.fair_total_spent = total_toronto_fair_cost_1
                            t_qs.special_request = extra_notes_toronto_fair_1
                            t_qs.package_type = select_booth_package(toronto_booth_option_1)
                            t_qs.save()
                            m.toronto_booking.add(t_qs)

                        elif index == 1:
                            t_qs.booth_option = toronto_booth_option_2
                            t_qs.additional_booth_option = toronto_additional_booth_option_2
                            t_qs.fair_total_spent = total_toronto_fair_cost_2
                            t_qs.special_request = extra_notes_toronto_fair_2
                            t_qs.package_type = select_booth_package(toronto_booth_option_2)
                            t_qs.save()
                            m.toronto_booking.add(t_qs)





            if 'Calgary' in select_cities:
                for index in range(0, len(calgaryList)):
                    if calgaryList[index] == '-':
                        print('Date Selection is "-" so fair is not in use.')
                    elif calgaryList[index] != '-':

                        c_qs = CalgaryFair(
                            related_sale=m,
                            date_selection=calgaryList[index],
                        )
                        if index == 0:
                            c_qs.booth_option = calgary_booth_option_1
                            c_qs.additional_booth_option = calgary_additional_booth_option_1
                            c_qs.additional_lunch_option = fix_lunch_issue(calgary_additional_lunch_option_1)
                            c_qs.wifi_for_device = wifi_option_calgary_fair_1
                            c_qs.diet_request = calgary_diet_request_1
                            c_qs.fair_total_spent = total_calgary_fair_cost_1
                            c_qs.special_request = extra_notes_calgary_fair_1
                            c_qs.electricity = check_boolean(electricty_option_calgary_1)
                            c_qs.package_type = select_booth_package(calgary_booth_option_1)
                            c_qs.save()
                            m.calgary_booking.add(c_qs)

                        elif index == 1:
                            c_qs.booth_option = calgary_booth_option_2
                            c_qs.additional_booth_option = calgary_additional_booth_option_2
                            c_qs.additional_lunch_option = fix_lunch_issue(calgary_additional_lunch_option_2)
                            c_qs.wifi_for_device = wifi_option_calgary_fair_2
                            c_qs.diet_request = calgary_diet_request_2
                            c_qs.fair_total_spent = total_calgary_fair_cost_2
                            c_qs.special_request = extra_notes_calgary_fair_2
                            c_qs.electricity = check_boolean(electricty_option_calgary_2)
                            c_qs.package_type = select_booth_package(calgary_booth_option_2)
                            c_qs.save()
                            m.calgary_booking.add(c_qs)

                        elif index == 2:
                            c_qs.booth_option = calgary_booth_option_3
                            c_qs.additional_booth_option = calgary_additional_booth_option_3
                            c_qs.additional_lunch_option = fix_lunch_issue(calgary_additional_lunch_option_3)
                            c_qs.wifi_for_device = wifi_option_calgary_fair_3
                            c_qs.diet_request = calgary_diet_request_3
                            c_qs.fair_total_spent = total_calgary_fair_cost_3
                            c_qs.special_request = extra_notes_calgary_fair_3
                            c_qs.electricity = check_boolean(electricty_option_calgary_3)
                            c_qs.package_type = select_booth_package(calgary_booth_option_3)
                            c_qs.save()
                            m.calgary_booking.add(c_qs)



            if 'Edmonton' in select_cities:
                for index in range(0, len(calgaryList)):
                    if edmontonList[index] == '-':
                        print('Date Selection is "-" so fair is not in use')
                    elif edmontonList[index] != '-':

                        e_qs = EdmontonFair(
                            related_sale=m,
                            date_selection=edmontonList[index],
                        )
                        if index == 0:
                            e_qs.booth_option = edmonton_booth_option_1
                            e_qs.additional_booth_option = edmonton_additional_booth_option_1
                            e_qs.additional_lunch_option = fix_lunch_issue(edmonton_additional_lunch_option_1)
                            e_qs.wifi_for_device = wifi_option_edmonton_fair_1
                            e_qs.diet_request = edmonton_diet_request_1
                            e_qs.fair_total_spent = total_edmonton_fair_cost_1
                            e_qs.special_request = extra_notes_edmonton_fair_1
                            e_qs.package_type = select_booth_package(edmonton_booth_option_1)
                            e_qs.save()
                            m.edmonton_booking.add(e_qs)

                        elif index == 1:
                            e_qs.booth_option = edmonton_booth_option_2
                            e_qs.additional_booth_option = edmonton_additional_booth_option_2
                            e_qs.additional_lunch_option = fix_lunch_issue(edmonton_additional_lunch_option_2)
                            e_qs.wifi_for_device = wifi_option_edmonton_fair_2
                            e_qs.diet_request = edmonton_diet_request_2
                            e_qs.fair_total_spent = total_edmonton_fair_cost_2
                            e_qs.special_request = extra_notes_edmonton_fair_2
                            e_qs.package_type = select_booth_package(edmonton_booth_option_2)
                            e_qs.save()
                            m.edmonton_booking.add(e_qs)

                        elif index == 2:
                            e_qs.booth_option = edmonton_booth_option_3
                            e_qs.additional_booth_option = edmonton_additional_booth_option_3
                            e_qs.additional_lunch_option = fix_lunch_issue(edmonton_additional_lunch_option_3)
                            e_qs.wifi_for_device = wifi_option_edmonton_fair_3
                            e_qs.diet_request = edmonton_diet_request_3
                            e_qs.fair_total_spent = total_edmonton_fair_cost_3
                            e_qs.special_request = extra_notes_edmonton_fair_3
                            e_qs.package_type = select_booth_package(edmonton_booth_option_3)
                            e_qs.save()
                            m.edmonton_booking.add(e_qs)

                        elif index == 3:
                            e_qs.booth_option = edmonton_booth_option_4
                            e_qs.additional_booth_option = edmonton_additional_booth_option_4
                            e_qs.additional_lunch_option = fix_lunch_issue(edmonton_additional_lunch_option_4)
                            e_qs.wifi_for_device = wifi_option_edmonton_fair_4
                            e_qs.fair_total_spent = total_edmonton_fair_cost_4
                            e_qs.special_request = extra_notes_edmonton_fair_4
                            e_qs.package_type = select_booth_package(edmonton_booth_option_4)
                            e_qs.save()
                            m.edmonton_booking.add(e_qs)


            if 'Winnipeg' in select_cities:
                for index in range(0, len(winnipegList)):
                    print(winnipegList)
                    if winnipegList[index] == '-':
                        print('Date Selection is "-" so fair is not in use')
                    elif winnipegList[index] != '-':

                        w_qs = WinnipegFair(
                            related_sale=m,
                            date_selection=winnipegList[index],
                        )

                        if index == 0:
                            w_qs.booth_option = winnipeg_booth_option_1
                            w_qs.additional_booth_option = winnipeg_additional_booth_option_1
                            w_qs.additional_lunch_option = fix_lunch_issue(winnipeg_additional_lunch_option_1)
                            w_qs.fair_total_spent = total_winnipeg_fair_cost_1
                            w_qs.special_request = extra_notes_winnipeg_fair_1
                            w_qs.package_type = select_booth_package(winnipeg_booth_option_1)
                            w_qs.save()
                            m.winnipeg_booking.add(w_qs)

                        if index == 1:
                            w_qs.booth_option = winnipeg_booth_option_2
                            w_qs.additional_booth_option = winnipeg_additional_booth_option_2
                            w_qs.additional_lunch_option = fix_lunch_issue(winnipeg_additional_lunch_option_2)
                            w_qs.fair_total_spent = total_winnipeg_fair_cost_2
                            w_qs.special_request = extra_notes_winnipeg_fair_2
                            w_qs.package_type = select_booth_package(winnipeg_booth_option_2)
                            w_qs.save()
                            m.winnipeg_booking.add(w_qs)
            m.save()

            return HttpResponseRedirect('/success')

        return render(request, self.template_name, {'form': PaymentForm()})