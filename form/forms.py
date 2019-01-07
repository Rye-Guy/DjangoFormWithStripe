from django import forms
from .models import SalesFormData

class PaymentForm(forms.ModelForm):

    class Meta:
        model = SalesFormData
        fields = ['company_name','contact_name','address','city_or_province','postal_code','contact_email','office_phone_number','direct_phone_number','facebook_link','website_link','twitter_link', 'calgary_diet_request', 'edmonton_diet_request', 'winnipeg_diet_request']

    CITY_CHOICES = (
        ('Toronto', 'Toronto'),
        ('Winnipeg', 'Winnipeg'),
        ('Calgary', 'Calgary'),
        ('Edmonton', 'Edmonton')
    )
    TORONTO_DATES = (
        ('TO APR-24-2018', 'April 24th, 2018'),
        ('TO SEPT-17-2019', 'September 17th, 2019')
    )

    CALGARY_DATES = (
        ('CAL MAR-12-2019', 'March 12th, 2019'),
        ('CAL JUN-26-2019', 'June 26th, 2019'),
        ('CAL OCT-22-2019', 'October 22nd, 2019')
    )

    EDMONTON_DATES = (
        ('EDM JAN-29-2019', 'January 29th, 2019'),
        ('EDM MAY-28-2019', 'May 28th, 2019'),
        ('EDM AUG-13-2019', 'August 13th, 2019'),
        ('EDM NOV-19-2019', 'November 19th, 2019')
    )
    WINNIPEG_DATES = (
        ('WIN JUL-10-2019', 'July 10th, 2019'),
        ('WIN APR-02-2019', 'April 2nd, 2019'),
        ('WIN JUL-23-2019', 'July 23rd, 2019')
    )


    TORONTO_BOOTH_OPTIONS = (
        ('2995', 'Platinum - $2995'),
        ('2495', 'Gold - $2495'),
        ('1995', 'Silver  - $1995'),
        ('1495', 'Bronze - $1495')
    )

    CALGARY_BOOTH_OPTIONS = (
        ('2995', 'Platinum - $2995'),
        ('2495', 'Gold - $2495'),
        ('1995', 'Silver - $1995'),
        ('1495', 'Bronze - $1495')
    )
    EDMONTON_BOOTH_OPTIONS = (
        ('2995', 'Platinum - $2995'),
        ('2495', 'Gold - $2495'),
        ('1995', 'Silver - $1995'),
        ('1495', 'Bronze - $1495')
    )
    WINNIPEG_BOOTH_OPTIONS = (
        ('2995', 'Platinum - $2995'),
        ('2495', 'Gold - $2495'),
        ('1995', 'Silver - $1995'),
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

    select_cities = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=CITY_CHOICES, required=False)

    toronto_dates = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'dates-select'}), choices=TORONTO_DATES, required=False)
    toronto_booth_options = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'booth-options-select'}), choices=TORONTO_BOOTH_OPTIONS, required=False)

    calgary_dates = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'dates-select'}), choices=CALGARY_DATES, required=False)
    calgary_booth_options = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'booth-options-select'}), choices=CALGARY_BOOTH_OPTIONS, required=False)
    calgary_options = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'fair-options'}), choices=CALGARY_FAIR_OPTIONS, required=False)

    edmonton_dates = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'dates-select'}), choices=EDMONTON_DATES, required=False)
    edmonton_booth_options = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'booth-options-select'}), choices=EDMONTON_BOOTH_OPTIONS, required=False)
    edmonton_options = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'fair-options'}),
                                                 choices=EDMONTON_FAIR_OPTIONS, required=False)

    winnipeg_dates = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'dates-select'}), choices=WINNIPEG_DATES, required=False)
    winnipeg_booth_options = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'booth-options-select'}), choices=WINNIPEG_BOOTH_OPTIONS, required=False)

    def clean(self):
        cleaned_data = super().clean()
        cities = cleaned_data.get('select_cities')

        def clean_city(self, city_name):
            city_dates = cleaned_data.get(city_name+'_dates')
            city_options = cleaned_data.get(city_name+'_booth_options')
            if not city_dates and city_options:
                self.add_error(city_name+'_dates', 'You have selected a booth option but not a date option!')
            if city_dates and not city_options:
                self.add_error(city_name+'_booth_options', 'You have selected a date but not a booth option!')
            if not city_dates and not city_options:
                self.add_error(city_name+'_dates', 'You not selected a date option!')
                self.add_error(city_name+'_booth_options', 'You have not selected a date option!')

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