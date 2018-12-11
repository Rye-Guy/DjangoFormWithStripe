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


def register(request):
    if request.method == "POST"
    if form.is_valid():
        try: 
            customer = stripe.charge.create(
                amount = 499,
                currency = CAD,
                description = form.cleaned_data['stripe_id']

            )

            form.saved()

            redirect('/register_success')
        except stripe.CardError, e:
            form.add_error('your card has been declined')

    else
        form = CustomUserForm()

    args = {}
    args.update(csrf(request))
    args['forms'] = form
  
def register_success(request):
    return render_to_response('register_success.html')  
