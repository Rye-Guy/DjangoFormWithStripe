from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
# Create your views here.

from form.forms import PaymentForm, CustomerModelFormClass

class IndexPageView(TemplateView):
    template_name = 'base-html.html'
    formPayment = PaymentForm()
    form_class = PaymentForm
    formContactInfo = CustomerModelFormClass()
    some_text = "YEAH! PUT SOME TEXT IN ME!!!"

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        context.update({'some_text': self.some_text, 'form': self.formPayment, 'customer_form': self.formContactInfo})
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print(request.POST)
        print(request.POST.get('price', ''))
        if form.has_error('select_cities'):
            pass
        if form.is_valid():
            print('valid')
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})

