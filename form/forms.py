from django import forms

class PaymentForm(forms.Form):
    CITY_CHOICES = (
        ('Toronto', 'Toronto'),
        ('Winnipeg', 'Winnipeg'),
        ('Calgary', 'Calgary'),
        ('Edmonton', 'Edmonton')
    )
    select_cities = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=CITY_CHOICES)
