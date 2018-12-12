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

    select_cities = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=CITY_CHOICES, required=False)



    toronto_dates = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'dates-select'}), choices=TORONTO_DATES, required=False)
    toronto_booth_options = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'booth-options-select'}), choices=TORONTO_BOOTH_OPTIONS, required=False)
    toronto_additional_booth_option = forms.ChoiceField(choices=((0,0),(1,1),(2,2),(3,3),(4,4),(5,5)))


    calgary_dates = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'dates-select'}), choices=CALGARY_DATES, required=False)
    calgary_booth_options = forms.MultipleChoiceField(widget=forms.RadioSelect(attrs={'class': 'booth-options-select'}), choices=CALGARY_BOOTH_OPTIONS, required=False)
    calgary_additional_booth_option = forms.ChoiceField(choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    calgary_additional_lunch_option = forms.ChoiceField(choices=((0,0),(1,1),(2,2),(3,3),(4,4),(5,5)))
    calgary_electricity_access = forms.BooleanField(label='Electricity Access?', required=False)
    calgary_internet_access = forms.BooleanField(label='Internet Access?', required=False)
    calgary_diet_request = forms.CharField(max_length=500, required=False)
    calgary_options = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'fair-options'}), choices=CALGARY_FAIR_OPTIONS, required=False)



    edmonton_dates = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'dates-select'}), choices=EDMONTON_DATES, required=False)
    edmonton_booth_options = forms.MultipleChoiceField(widget=forms.RadioSelect(attrs={'class': 'booth-options-select'}), choices=EDMONTON_BOOTH_OPTIONS, required=False)
    edmonton_additional_booth_option = forms.ChoiceField(choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    edmonton_additional_lunch_option = forms.ChoiceField(choices=((0,0),(1,1),(2,2),(3,3),(4,4),(5,5)))
    edmonton_additional_breakfast_option = forms.ChoiceField(choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    edmonton_diet_request = forms.CharField(max_length=500, required=False)
    edmonton_options = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'fair-options'}),
                                                 choices=EDMONTON_FAIR_OPTIONS, required=False)



    winnipeg_dates = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'dates-select'}), choices=WINNIPEG_DATES, required=False)
    winnipeg_booth_options = forms.MultipleChoiceField(widget=forms.RadioSelect(attrs={'class': 'booth-options-select'}), choices=WINNIPEG_BOOTH_OPTIONS, required=False)
    winnipeg_additional_booth_option = forms.ChoiceField(choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    winnipeg_additional_lunch_option = forms.ChoiceField(choices=((0,0),(1,1),(2,2),(3,3),(4,4),(5,5)))
    winnipeg_diet_request = forms.CharField(max_length=500, required=False)

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        cities = cleaned_data.get('select_cities')
        print(cities)

        def get_cities(self, *args, **kwargs):
            if cities == []:
                raise forms.ValidationError({'select_cities': 'Please Select at Least One City'}, code='invalid')
            else:
                return self

        def clean_city(self, city_name):
            city_dates = cleaned_data.get(city_name+'_dates')
            city_options = cleaned_data.get(city_name+'_booth_options')
            if not city_dates and city_options:
                raise forms.ValidationError({city_name+'_dates': 'You have selected a booth option but not a date option!'})
            if city_dates and not city_options:
                raise forms.ValidationError({city_name+'_booth_options': 'You have selected a date but not a booth option!'})
            if not city_dates and not city_options:
                raise forms.ValidationError({city_name+'_dates': 'You not selected a date option!', city_name+'_booth_options': 'You have not selected a date option!'})
            return self


        if cities == []:
            raise forms.ValidationError({'select_cities': 'Please Select at Least One City'}, code='invalid')
        if 'Toronto' and 'Winnipeg' and 'Calgary' and 'Edmonton' in cities:
            clean_city(self, 'toronto')
        if 'Winnipeg' in cities:
            clean_city(self, 'winnipeg')
        if 'Calgary' in cities:
            clean_city(self, 'calgary')
        if 'Edmonton' in cities:
            clean_city(self, 'edmonton')
