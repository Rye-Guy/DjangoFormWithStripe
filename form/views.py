from django.conf import settings
from django.shortcuts import render
from django.views.generic.base import TemplateView

from form.forms import PaymentForm, CustomerModelFormClass

import datetime
import stripe

stripe.api_key = settings.SECRET_KEY


class IndexPageView(TemplateView):
    template_name = 'base-html.html'
    formPayment = PaymentForm()
    formContactInfo = CustomerModelFormClass()
    some_text = "YEAH! PUT SOME TEXT IN ME!!!"

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        context.update({'some_text': self.some_text, 'form': self.formPayment, 'customer_form': self.formContactInfo})
        return context


    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

def charge(request): # new
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='cad',
            description='A Django stripe charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'register_success.html')