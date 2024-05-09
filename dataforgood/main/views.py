from django.shortcuts import render
from django.template.defaulttags import register

from .forms import SearchForm, SubgroupForm
from .utils import create_subgroup_tables, create_table, create_table_title


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


# Main Page - /main/
def index(request):
    return render(request, "index.html")


# About Us Page - /main/about_us/
def aboutus(request):
    return render(request, "aboutus.html")


# MODIFIED LINE 44 and 50
# Data and Visualize with FORMS - /main/data&visualize/
def dataandvisualize(request):
    if request.method == "GET":
        form = SearchForm(request.GET)
        subgroup_form = SubgroupForm(year_choices=[])

        if form.is_valid():
            # Extract variables from SearchForm
            geograpahic_level = form.cleaned_data["geographic_level"]
            geographic_unit = form.cleaned_data["tract"]
            category = form.cleaned_data["category"]
            indicator = form.cleaned_data["indicator"]
            year = form.cleaned_data["year"]
            subgroup_form = SubgroupForm(
                year_choices=[
                    (str(year), str(year)) for year in form.cleaned_data["year"]
                ]
            )
            # Create main table context variables
            table_title = create_table_title(indicator, year)
            field = create_table(
                geograpahic_level, geographic_unit, indicator, year
            )

            # Create subtable context variables
            multi_year_subtable_field = create_subgroup_tables(
                geograpahic_level, geographic_unit, indicator, year
            )
            print(multi_year_subtable_field)

            # Hardcoding subtable title for testing
            str(year[0])

            # Prepare data for the chart
            chart_data = {
                "categories": field["headers"][1:],  # Years
                "series": [],
            }
            for row in field["rows"]:
                chart_data["series"].append(
                    {
                        "name": row[0],  # Geographic unit
                        "data": row[1:],  # Values for each year
                    }
                )

            context = {
                "field": field,
                "table_title": table_title,
                "multi_year_subtable_field": multi_year_subtable_field,
                "chart_data": chart_data,
                "subgroup_form": subgroup_form,
            }
            return render(request, "dataandvisualize.html", context)

    return render(
        request,
        "dataandvisualize.html",
        {"form": form, "subgroup_form": SubgroupForm(year_choices=[])},
    )


# Resources Page - /main/resources/
def resources(request):
    return render(request, "resources.html")
