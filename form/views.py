from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

from form.forms import PaymentForm, CustomerModelFormClass

class IndexPageView(TemplateView):
    template_name = 'base-html.html'
    formPayment = PaymentForm()
    formContactInfo = CustomerModelFormClass()
    some_text = "YEAH! PUT SOME TEXT IN ME!!!"

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        context.update({'some_text': self.some_text, 'form': self.formPayment, 'customer_form': self.formContactInfo})
        return context


