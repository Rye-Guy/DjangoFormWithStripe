from django import forms

class PaymentForm(forms.Form):
    CITY_CHOICES = (
        ('Toronto', 'Toronto'),
        ('Winnipeg', 'Winnipeg'),
        ('Calgary', 'Calgary'),
        ('Edmonton', 'Edmonton')
    )
    TORONTO_DATES = (
        ('date1', 'September 19th, 2018'),
        ('date2', 'April 24th, 2018'),
        ('date3', 'September 17h, 2019')
    )

    TORONTO_FAIR_OPTIONS = (
        ('option1', 'Electricity'),
        ('option2', 'Wifi')
    )
    CALGARY_DATES = (
        ('date1', 'March 12th, 2019'),
        ('date2', 'June 26th, 2019'),
        ('date3', 'October 22nd, 2019')
    )

    CALGARY_FAIR_OPTIONS = (
        ('option1', 'Extra Lunch'),
        ('option2', 'Access to Electricity'),
        ('option3', 'Special Diet Request'),
        ('option4', 'Internet Access')
    )
    EDMONTON_DATES = (
        ('date1', 'January 29th, 2019'),
        ('date2', 'May 28th, 2019'),
        ('date3', 'August 13th, 2019'),
        ('date3', 'November 19th, 2019')
    )

    EDMONTON_FAIR_OPTIONS = (
        ('option1', 'Extra Breakfast'),
        ('option2', 'Extra Lunch'),
        ('option3', 'Special Diet Request'),
        ('option4', 'Access to Electricity'),
        ('option5', 'Internet Access')
    )
    WINNIPEG_DATES = (
        ('date1', 'July 10th, 2019'),
        ('date2', 'April 2nd, 2019'),
        ('date3', 'July 23rd, 2019')
    )

    WINNIPEG_FAIR_OPTIONS = (
        ('option1', 'Extra Lunch'),
        ('option5', 'Internet Access')
    )

    TORONTO_BOOTH_OPTIONS = (
        ('booth', 'All Booths - $1995')
    )

    CALGARY_BOOTH_OPTIONS = (
        ('booth1', 'Platinum - $2995'),
        ('booth2', 'Gold - $2495'),
        ('booth3', 'Silver - $1995'),
        ('booth4', 'Bronze - $1495')
    )
    EDMONTON_BOOTH_OPTIONS = (
        ('booth1', 'Platinum - $2995'),
        ('booth2', 'Gold - $2495'),
        ('booth3', 'Silver - $1995'),
        ('booth4', 'Bronze - $1495')
    )
    WINNIPEG_BOOTH_OPTIONS = (
        ('booth1', 'Platinum - $2995'),
        ('booth2', 'Gold - $2495'),
        ('booth3', 'Silver - $1995'),
        ('booth4', 'Bronze - $1495')
    )



    select_cities = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=CITY_CHOICES)
    toronto_dates = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=TORONTO_DATES)
    toronto_booth_options = forms.BooleanField(label='All Booths - $1995')
    toronto_options = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=TORONTO_FAIR_OPTIONS)
    calgary_dates = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=CALGARY_DATES)
    calgary_booth_options = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=CALGARY_BOOTH_OPTIONS)
    calgary_options = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=CALGARY_FAIR_OPTIONS)
    edmonton_dates = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=EDMONTON_DATES)
    edmonton_booth_options = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=EDMONTON_BOOTH_OPTIONS)
    edmonton_options = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                            choices=EDMONTON_FAIR_OPTIONS)
    winnipeg_dates = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=WINNIPEG_DATES)
    winnipeg_booth_options = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=WINNIPEG_BOOTH_OPTIONS)
    winnipeg_options = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                        choices=WINNIPEG_FAIR_OPTIONS)