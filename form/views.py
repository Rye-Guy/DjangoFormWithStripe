from django.conf import settings
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
# Create your views here.

from form.forms import PaymentForm, CustomerModelFormClass

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
        price = request.POST.get('price', '')
        if form.is_valid() and customer_form.is_valid():
            print('valid form data')
            # stripe.Charge.create(
            #     amount=price,
            #     currency='cad',
            #     description='Django stripe charge',
            #     source=request.POST['stripeToken']
            # )
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form, 'customer_form': customer_form})

