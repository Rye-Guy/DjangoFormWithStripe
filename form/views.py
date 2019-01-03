from django.conf import settings
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect, QueryDict
# Create your views here.

from form.forms import PaymentForm, CustomerModelFormClass
from form.models import SalesFormData

import stripe

class IndexPageView(TemplateView):
    template_name = 'base-html.html'
    formPayment = PaymentForm()
    form_class = PaymentForm
    formContactInfo = CustomerModelFormClass()
    customerFormClass = CustomerModelFormClass
    some_text = "YEAH! PUT SOME TEXT IN ME!!!"
    stripeApiKey = settings.STRIPE_SECRET_KEY

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        context.update({'some_text': self.some_text, 'form': self.formPayment, 'customer_form': self.formContactInfo})
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        customer_form = self.customerFormClass(request.POST)
        print(request.POST)
        if form and customer_form:


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
            toronto_dates = request.POST.getlist('toronto_dates')
            select_cities = request.POST.getlist('select_cities')

            select_cities_for_db = ', '.join(select_cities)


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
                toronto_dates=toronto_dates)

            m.save()


            # stripe.Charge.create(
            #     amount=price,
            #     currency='cad',
            #     description='Django stripe charge',
            #     source=request.POST['stripeToken']
            # )
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form, 'customer_form': customer_form})

