from django import forms

from .models import EconomicMain, Georeference
from .utils import get_choices


class SearchForm(forms.Form):
    geographic_level = forms.ChoiceField(
        choices=[
            ("City of Chicago", "City of Chicago"),
            ("Community Area", "Community Area"),
            ("Zipcode", "Zipcode"),
            ("Tract", "Tract"),
        ],
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    tract = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=get_choices(Georeference, "id"),
    )

    category = indicator = forms.ChoiceField(
        choices=[
            ("Economic", "Economic"),
            ("Education", "Education"),
            ("Health", "Health"),
            ("Housing", "Housing"),
            ("Population", "Population"),
        ],
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    indicator = forms.ChoiceField(
        choices=get_choices(EconomicMain, "indicator_name"),
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    year = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=get_choices(EconomicMain, "year"),
    )


class SubgroupForm(forms.Form):
    subgroup_year = forms.ChoiceField(
        choices=[], widget=forms.Select(attrs={"class": "form-control"})
    )

    def __init__(self, year_choices, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["subgroup_year"].choices = year_choices
