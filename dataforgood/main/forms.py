from django import forms

from .models import CensusTracts, ContractRent_Main
# from .models2 import *
from .utils import get_choices

# Category chocies
CATEGORY_CHOCIES = [
            ("Economic", "Economic"),
            ("Education", "Education"),
            ("Health", "Health"),
            ("Housing", "Housing"),
            ("Population", "Population"),
        ]

# Geographic level choices
GEOGRAPHIC_LEVEL_CHOICES = [
            ("City of Chicago", "City of Chicago"),
            ("Community Area", "Community Area"),
            ("Zipcode", "Zipcode"),
            ("Tract", "Tract"),
        ]

# Indicator chocies for each category

ECONOMIC_CHOCIES = [
    ('Median Income in the Past 12 Months (inflation-adjusted)',
    'Median Income in the Past 12 Months (inflation-adjusted)'),
    ('Mean Income in the Past 12 Months (inflation-adjusted)',
    'Mean Income in the Past 12 Months (inflation-adjusted)'),
    ]

HOUSING_CHOICES = [
    ('Aggregate Contract Rent',
     'Aggregate Contract Rent'),
    ('Total Number of Households',
     'Total Number of Households'),
    ]

EDUCATION_CHOICES = [
    ('Median Earnings in the Past 12 Months', 
     'Median Earnings in the Past 12 Months'),
    ('Population 3 years and over enrolled in school',
     'Population 3 years and over enrolled in school'),
    ]

HEALTH_CHOICES = [
    ('Total Population With Disability',
     'Total Population With Disability'),
    ('Insurance Coverage: Total Population',
     'Insurance Coverage: Total Population'),
    ]

POPULATION_CHOICES = [
    ('Total Population and Race Group',
     'Total Population and Race Group'),
    ('Median Age',
     'Median Age'),
    ]


class SearchForm(forms.Form):
    geographic_level = forms.ChoiceField(
        choices=GEOGRAPHIC_LEVEL_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    tract = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=get_choices(CensusTracts, "tract_id"),
    )

    category = indicator = forms.ChoiceField(
        choices=CATEGORY_CHOCIES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    # To be modified to become dynamic depending on category selected by user
    indicator = forms.ChoiceField(
        choices=get_choices(ContractRent_Main, "indicator_name"),
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    # To be modified to become dyanmic dependin gon the indicator selected by user
    year = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=get_choices(ContractRent_Main, "year"),
    )


class SubgroupForm(forms.Form):
    subgroup_year = forms.ChoiceField(
        choices=[], widget=forms.Select(attrs={"class": "form-control"})
    )

    def __init__(self, year_choices, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["subgroup_year"].choices = year_choices
