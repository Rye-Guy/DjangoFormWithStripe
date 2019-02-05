from django import forms
from django.forms import ChoiceField
from .models import SalesFormData

class PaymentForm(forms.ModelForm):

    CITY_CHOICES = (
        ('Toronto', 'Toronto'),
        ('Winnipeg', 'Winnipeg'),
        ('Calgary', 'Calgary'),
        ('Edmonton', 'Edmonton')
    )
    TORONTO_DATES = (
        ('04-24-2019', 'April 24th, 2018'),
        ('09-17-2019', 'September 17th, 2019')
    )

    CALGARY_DATES = (
        ('03-12-2019', 'March 12th, 2019'),
        ('06-26-2019', 'June 26th, 2019'),
        ('10-22-2019', 'October 22nd, 2019')
    )

    EDMONTON_DATES = (
        ('01-29-2019', 'January 29th, 2019'),
        ('05-28-2019', 'May 28th, 2019'),
        ('08-13-2019', 'August 13th, 2019'),
        ('11-19-2019', 'November 19th, 2019')
    )
    CITY_CHOICES = (
        ('Toronto', 'Toronto'),
        ('Winnipeg', 'Winnipeg'),
        ('Calgary', 'Calgary'),
        ('Edmonton', 'Edmonton')
    )
    TORONTO_DATES = (
        ('04-24-2019', 'April 24th, 2018'),
        ('09-17-2019', 'September 17th, 2019')
    )

    CALGARY_DATES = (
        ('03-12-2019', 'March 12th, 2019'),
        ('06-26-2019', 'June 26th, 2019'),
        ('10-22-2019', 'October 22nd, 2019')
    )

    EDMONTON_DATES = (
        ('01-29-2019', 'January 29th, 2019'),
        ('05-28-2019', 'May 28th, 2019'),
        ('08-13-2019', 'August 13th, 2019'),
        ('11-19-2019', 'November 19th, 2019')
    )
    WINNIPEG_DATES = (
        ('04-02-2019', 'April 2nd, 2019'),
        ('07-10-2019', 'July 10th, 2019'),
        ('07-23-2019', 'July 23rd, 2019')
    )

    BOOTH_OPTIONS = (
        ('2995', 'Platinum - $2995'),
        ('2495', 'Gold - $2495'),
        ('1995', 'Silver  - $1995'),
        ('1495', 'Bronze - $1495')
    )

    CALGARY_FAIR_OPTIONS = (
        ('Electricity', 'Access to Electricity'),
        ('Internet', 'Internet Access')
    )

    EDMONTON_FAIR_OPTIONS = (
        ('Electricity', 'Access to Electricity'),
        ('Internet', 'Internet Access')
    )

    class Meta:
        PROVINCE_CHOICES = (
            ('-', '-'),
            ('Alberta', 'Alberta'),
            ('British Columbia', 'British Columbia'),
            ('Manitoba', 'Manitoba'),
            ('New Brunswick', 'New Brunswick'),
            ('Newfoundland and Labrador', 'Newfoundland and Labrador'),
            ('Nova Scotia', 'Nova Scotia'),
            ('Ontario', 'Ontario'),
            ('Prince Edward Island', 'Prince Edward Island'),
            ('Quebec', 'Quebec'),
            ('Saskatchewan', 'Saskatchewan'),
            ('Yukon', 'Yukon'),
            ('Northwest Territories', 'Northwest Territories'),
            ('Nunavut', 'Nunavut')
        )
        model = SalesFormData
        
        fields = ['sales_rep','company_name','contact_name','address','secondary_address','city','province','postal_code','contact_email','office_phone_number','direct_phone_number','facebook_link','website_link','twitter_link', 'discount_amount']
        widgets = {
            'province' : forms.Select(choices=PROVINCE_CHOICES)
        }
    


    select_cities = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'btn'}), choices=CITY_CHOICES, required=False)

    toronto_dates = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'dates-select'}), choices=TORONTO_DATES, required=False)
    # toronto_booth_options = forms.ChoiceField(widget=forms.Select(attrs={'class': 'booth-options-select'}), choices=BOOTH_OPTIONS, required=False)

    calgary_dates = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'dates-select'}), choices=CALGARY_DATES, required=False)
    calgary_options = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'fair-options'}), choices=CALGARY_FAIR_OPTIONS, required=False)

    edmonton_dates = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'dates-select'}), choices=EDMONTON_DATES, required=False)
    edmonton_options = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'fair-options'}),choices=EDMONTON_FAIR_OPTIONS, required=False)

    winnipeg_dates = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'dates-select'}), choices=WINNIPEG_DATES, required=False)

    def clean(self):
        cleaned_data = super().clean()
        cities = cleaned_data.get('select_cities')

        def clean_city(self, city_name):
            city_dates = cleaned_data.get(city_name+'_dates')
            # city_options = cleaned_data.get(city_name+'_booth_options')
            if not city_dates:
                self.add_error(city_name+'_dates', 'You have selected a fair date.')


        if cities == []:
            self.add_error('select_cities', 'You have not selected any fair locations!')
        if 'Toronto' in cities:
            clean_city(self, 'toronto')
        if 'Winnipeg' in cities:
            clean_city(self, 'winnipeg')
        if 'Calgary' in cities:
            clean_city(self, 'calgary')
        if 'Edmonton' in cities:
            clean_city(self, 'edmonton')


