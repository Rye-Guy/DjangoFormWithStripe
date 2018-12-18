from django.conf import settings
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
# Create your views here.

from form.forms import PaymentForm, CustomerModelFormClass

import datetime
import stripe

class IndexPageView(TemplateView):
    template_name = 'base-html.html'
    formPayment = PaymentForm()
    form_class = PaymentForm
    formContactInfo = CustomerModelFormClass()
    some_text = "YEAH! PUT SOME TEXT IN ME!!!"
    stripeApiKey = settings.STRIPE_SECRET_KEY

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        context.update({'some_text': self.some_text, 'form': self.formPayment, 'customer_form': self.formContactInfo})
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print(request.POST)
        price = request.POST.get('price', '')
        if form.has_error('select_cities'):
            form.add_error(self, form.select_cities)
        if form.is_valid():
            print('valid')
            charge = stripe.Charge.create(
                amount=price,
                currency='cad',
                description='Django stripe charge',
                source=request.POST['stripeToken']
            )
            return HttpResponseRedirect('/payment.html')

        return render(request, self.template_name, {'form': form})

