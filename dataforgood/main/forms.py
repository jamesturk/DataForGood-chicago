from django import forms

from .models import CensusTracts, TractZipCode

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
    ("2018-2022", "2018-2022"),
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

YES_NO_CHOICE = [("No", "No"), ("Yes", "Yes")]

# Indicator chocies for each category
category_to_indicators = {
    "Economic": ECONOMIC_CHOCIES,
    "Education": EDUCATION_CHOICES,
    "Health": HEALTH_CHOICES,
    "Housing": HOUSING_CHOICES,
    "Population": POPULATION_CHOICES,
}


class SearchForm(forms.Form):
    """
    A form class for handling user selections on the search page.

    Attributes:
        geographic_level (ChoiceField): A dropdown field for selecting the geographic level.
        tract (MultipleChoiceField): A multiple choice field for selecting census tracts.
        zipcode (MultipleChoiceField): A multiple choice field for selecting zip codes.
        community (MultipleChoiceField): A multiple choice field for selecting communities.
        category (ChoiceField): A dropdown field for selecting the data category.
        economic_indicators (MultipleChoiceField): A multiple choice field for selecting economic indicators.
        education_indicators (MultipleChoiceField): A multiple choice field for selecting education indicators.
        health_indicators (MultipleChoiceField): A multiple choice field for selecting health indicators.
        housing_indicators (MultipleChoiceField): A multiple choice field for selecting housing indicators.
        population_indicators (MultipleChoiceField): A multiple choice field for selecting population indicators.
        year (MultipleChoiceField): A multiple choice field for selecting the year(s) of data.
        generate_memo (ChoiceField): A dropdown field for selecting whether to generate a memo.

    Methods:
        __init__(self, *args, **kwargs): Initializes the form and sets the required attribute of certain fields to False.

    Helper Functions:
        create_multiple_choice_geo: Creates a multiple choice field for geographic selections.
        create_multiple_choice_indicator: Creates a multiple choice field for indicator selections.

    Form Fields:
        - geographic_level: A dropdown field for selecting the geographic level.
        - tract: A multiple choice field for selecting census tracts.
        - zipcode: A multiple choice field for selecting zip codes.
        - community: A multiple choice field for selecting communities.
        - category: A dropdown field for selecting the data category.
        - economic_indicators: A multiple choice field for selecting economic indicators.
        - education_indicators: A multiple choice field for selecting education indicators.
        - health_indicators: A multiple choice field for selecting health indicators.
        - housing_indicators: A multiple choice field for selecting housing indicators.
        - population_indicators: A multiple choice field for selecting population indicators.
        - year: A multiple choice field for selecting the year(s) of data.
        - generate_memo: A dropdown field for selecting whether to generate a memo.
    """

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
        self.fields["generate_memo"].required = False

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

    generate_memo = forms.ChoiceField(
        widget=forms.Select,
        choices=YES_NO_CHOICE,
    )


class SubgroupForm(forms.Form):
    """
    A form class for handling subgroup selections based on the available years.

    Attributes:
        subgroup_year (ChoiceField): A dropdown field for selecting the subgroup year.

    Methods:
        __init__(self, year_choices, *args, **kwargs): Initializes the form and sets the choices for the subgroup_year field based on the provided year_choices.

    Form Fields:
        - subgroup_year: A dropdown field for selecting the subgroup year.

    Note:
        - The choices for the subgroup_year field are dynamically set based on the year_choices provided during form initialization.
    """

    subgroup_year = forms.ChoiceField(
        choices=[], widget=forms.Select(attrs={"class": "form-control"})
    )

    def __init__(self, year_choices, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["subgroup_year"].choices = year_choices
