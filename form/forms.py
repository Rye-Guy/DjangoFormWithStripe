from django import forms
from .models import CustomerModelForm

class CustomerModelFormClass(forms.ModelForm):
    class Meta:
        model = CustomerModelForm
        fields = '__all__'#['company_name', 'contact_name']

class PaymentForm(forms.Form):

    CITY_CHOICES = (
        ('Toronto', 'Toronto'),
        ('Winnipeg', 'Winnipeg'),
        ('Calgary', 'Calgary'),
        ('Edmonton', 'Edmonton')
    )
    TORONTO_DATES = (
        ('date1', 'April 24th, 2018'),
        ('date2', 'September 17h, 2019')
    )

    CALGARY_DATES = (
        ('date1', 'March 12th, 2019'),
        ('date2', 'June 26th, 2019'),
        ('date3', 'October 22nd, 2019')
    )

    EDMONTON_DATES = (
        ('date1', 'January 29th, 2019'),
        ('date2', 'May 28th, 2019'),
        ('date3', 'August 13th, 2019'),
        ('date3', 'November 19th, 2019')
    )
    WINNIPEG_DATES = (
        ('date1', 'July 10th, 2019'),
        ('date2', 'April 2nd, 2019'),
        ('date3', 'July 23rd, 2019')
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
        ('option1', 'Access to Electricity'),
        ('option2', 'Internet Access')
    )

    EDMONTON_FAIR_OPTIONS = (
        ('option1', 'Access to Electricity'),
        ('option2s', 'Internet Access')
    )

    select_cities = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=CITY_CHOICES)



    toronto_dates = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'dates-select'}), choices=TORONTO_DATES)
    toronto_booth_options = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'booth-options-select'}), choices=TORONTO_BOOTH_OPTIONS, required=False)
    toronto_additional_booth_option = forms.ChoiceField(choices=((0,0),(1,1),(2,2),(3,3),(4,4),(5,5)))


    calgary_dates = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'dates-select'}), choices=CALGARY_DATES)
    calgary_booth_options = forms.MultipleChoiceField(widget=forms.RadioSelect(attrs={'class': 'booth-options-select'}), choices=CALGARY_BOOTH_OPTIONS, required=False)
    calgary_additional_booth_option = forms.ChoiceField(choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    calgary_additional_lunch_option = forms.ChoiceField(choices=((0,0),(1,1),(2,2),(3,3),(4,4),(5,5)))
    calgary_electricity_access = forms.BooleanField(label='Electricity Access?')
    calgary_internet_access = forms.BooleanField(label='Internet Access?')
    calgary_diet_request = forms.CharField(max_length=500, required=False)
    calgary_options = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'fair-options'}), choices=CALGARY_FAIR_OPTIONS)



    edmonton_dates = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'dates-select'}), choices=EDMONTON_DATES)
    edmonton_booth_options = forms.MultipleChoiceField(widget=forms.RadioSelect(attrs={'class': 'booth-options-select'}), choices=EDMONTON_BOOTH_OPTIONS, required=False)
    edmonton_additional_booth_option = forms.ChoiceField(choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    edmonton_additional_lunch_option = forms.ChoiceField(choices=((0,0),(1,1),(2,2),(3,3),(4,4),(5,5)))
    edmonton_additional_breakfast_option = forms.ChoiceField(choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    edmonton_diet_request = forms.CharField(max_length=500, required=False)
    edmonton_options = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'fair-options'}),
                                                 choices=EDMONTON_FAIR_OPTIONS)



    winnipeg_dates = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'dates-select'}), choices=WINNIPEG_DATES)
    winnipeg_booth_options = forms.MultipleChoiceField(widget=forms.RadioSelect(attrs={'class': 'booth-options-select'}), choices=WINNIPEG_BOOTH_OPTIONS, required=False)
    winnipeg_additional_booth_option = forms.ChoiceField(choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    winnipeg_additional_lunch_option = forms.ChoiceField(choices=((0,0),(1,1),(2,2),(3,3),(4,4),(5,5)))
    winnipeg_diet_request = forms.CharField(max_length=500, required=False)

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        cities = cleaned_data.get('select_cities')
        print(cities)

        def clean_toronto(self, *args, **kwargs):
            toronto_dates = cleaned_data.get('toronto_dates')
            toronto_options = cleaned_data.get('toronto_booth_options')
            if toronto_dates and not toronto_options:
                raise forms.ValidationError({'toronto_booth_options': 'You have selected a date but not a booth option!'})

        if cities == None:
            raise forms.ValidationError({'select_cities': 'Please Select at Least One City'}, code='invalid')
        if 'Toronto' in cities:
            clean_toronto(self)
            raise forms.ValidationError({'select_cities': 'Dont Select Toronto'}, code='invalid')
        if 'winnipeg' in cities:
            pass






