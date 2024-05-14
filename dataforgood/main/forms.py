from django import forms

from .models import CensusTracts, ContractRent_Main, TractZipCode

# from .models2 import *
from .utils import *


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
    ("Community", "Community"),
    ("Zipcode", "Zipcode"),
    ("Tract", "Tract"),
]

# Year choices
PERIOD_CHOICES = [
    ("2013-2017", "2013-2017"),
    ("2014-2018", "2014-2018"),
    ("2015-2019", "2015-2019"),
    ("2016-2020", "2016-2020"),
    ("2017-2021", "2017-2021"),
    ("2018-2022", "2018-2022")
]

# Indicator Choices
ECONOMIC_CHOCIES = [
    (
        "Median Income in the Past 12 Months (inflation-adjusted)",
        "Median Income in the Past 12 Months (inflation-adjusted)",
    ),
    (
        "Mean Income in the Past 12 Months (inflation-adjusted)",
        "Mean Income in the Past 12 Months (inflation-adjusted)",
    ),
]

HOUSING_CHOICES = [
    ("Aggregate Contract Rent", "Aggregate Contract Rent"),
    ("Total Number of Households", "Total Number of Households"),
]

EDUCATION_CHOICES = [
    (
        "Median Earnings in the Past 12 Months",
        "Median Earnings in the Past 12 Months",
    ),
    (
        "Population 3 years and over enrolled in school",
        "Population 3 years and over enrolled in school",
    ),
]

HEALTH_CHOICES = [
    ("Total Population With Disability", "Total Population With Disability"),
    (
        "Insurance Coverage: Total Population",
        "Insurance Coverage: Total Population",
    ),
]

POPULATION_CHOICES = [
    ("Total Population and Race Group", "Total Population and Race Group"),
    ("Median Age", "Median Age"),
]

# Indicator chocies for each category
category_to_indicators = {
    "Economic": ECONOMIC_CHOCIES,
    "Education": EDUCATION_CHOICES,
    "Health": HEALTH_CHOICES,
    "Housing": HOUSING_CHOICES,
    "Population": POPULATION_CHOICES,
}


class SearchForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields["tract"].required = False
        self.fields["zipcode"].required = False
        self.fields["community"].required = False
        self.fields["category"].required = False
        self.fields["economic_indicators"].required = False
        self.fields["health_indicators"].required = False
        self.fields["housing_indicators"].required = False
        self.fields["population_indicators"].required = False

    geographic_level = forms.ChoiceField(
        choices=GEOGRAPHIC_LEVEL_CHOICES,
        widget=forms.Select(
            attrs={"class": "form-control", "id": "id_geographic_level"}
        ),
    )

    tract = create_multiple_choice_geo(CensusTracts, "tract_id", "id_tract")
    zipcode = create_multiple_choice_geo(TractZipCode, "zip_code", "id_zipcode")
    community = create_multiple_choice_geo(
        CensusTracts, "community", "id_community"
    )

    category = forms.ChoiceField(
        choices=CATEGORY_CHOCIES,
        widget=forms.Select(
            attrs={"class": "form-control", "id": "id_category"}
        ),
    )

    economic_indicators = create_multiple_choice_indicator(
        ECONOMIC_CHOCIES, "id_economic_indicators"
    )
    education_indicators = create_multiple_choice_indicator(
        EDUCATION_CHOICES, "id_education_indicators"
    )
    health_indicators = create_multiple_choice_indicator(
        HEALTH_CHOICES, "id_health_indicators"
    )
    housing_indicators = create_multiple_choice_indicator(
        HOUSING_CHOICES, "id_housing_indicators"
    )
    population_indicators = create_multiple_choice_indicator(
        POPULATION_CHOICES, "id_population_indicators"
    )

    year = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=PERIOD_CHOICES,
    )


class SubgroupForm(forms.Form):
    subgroup_year = forms.ChoiceField(
        choices=[], widget=forms.Select(attrs={"class": "form-control"})
    )

    def __init__(self, year_choices, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["subgroup_year"].choices = year_choices
