import os
import uuid

import environ
import folium
import geopandas as gpd
import numpy as np
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaulttags import register
from django.views.decorators.csrf import csrf_protect

from dataforgood.settings import BASE_DIR

from .forms import SearchForm, SubgroupForm
from .utils import (
    MainTable,
    SubgroupTable,
    MAIN_MODEL_MAPPING,
    SUB_MODEL_MAPPING,
    WriteMemo,
    save_memo,
    generate_heatmaps,
    prepare_chart_data,
    prepare_subgroup_chart_data
)

env = environ.Env()
environ.Env.read_env()
open_ai_key = env("open_ai_key")

# Centroid of Chicago for heat map
y_center = 41.8781
x_center = -87.6298


@register.filter
def get_item(dictionary, key):
    """
    Retrieves the value associated with the specified key from the given dictionary.

    Args:
        dictionary (dict): The dictionary to retrieve the value from.
        key: The key to lookup in the dictionary.

    Returns:
        The value associated with the key in the dictionary, or None if the key is not found.
    """
    return dictionary.get(key)


# Main Page - /main/ ?do we still need it?
def index(request):
    return render(request, "index.html")


# About Us Page - /main/about_us/
def aboutus(request):
    """
    Renders the About Us page of the application.

    This function handles the request for the About Us page URL (/main/about_us/) and renders the "aboutus.html" template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered "aboutus.html" template as an HTTP response.
    """
    return render(request, "aboutus.html")


# MODIFIED LINE 44 and 50
# Data and Visualize with FORMS - /main/data&visualize/
@csrf_protect
def dataandvisualize(request):
    """
    Renders the data and visualization page of the application.

    This function handles the request for the data and visualization page URL (/main/dataandvisualize/).
    It processes the user's selections from the search form, retrieves the corresponding data, and generates
    visualizations based on the selected parameters.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered "dataandvisualize.html" template with the processed data and visualizations.

    Functionality:
        1. Initializes the search form and subgroup form.
        2. Handles the GET request and validates the form data.
        3. Extracts the selected variables from the search form.
        4. Creates the main table and subgroup tables based on the selected parameters.
        5. Prepares data for the main chart and subgroup charts.
        6. Generates heat maps for Community Area, Zip Code, and Tract levels.
        7. If selected, generates a memo about the data using the WriteMemo class and saves it.
        8. Renders the "dataandvisualize.html" template with the processed data, visualizations, and memo (if generated).

    Template:
        - dataandvisualize.html: The template file for displaying the data and visualizations.

    Form Classes:
        - SearchForm: The form class for handling user selections.
        - SubgroupForm: The form class for handling subgroup selections.

    Helper Functions:
        - create_table_title: Creates the title for the main table.
        - create_table: Creates the main table based on the selected parameters.
        - create_subgroup_tables: Creates the subgroup tables based on the selected parameters.
        - generate_heatmaps: Generates heatmaps based on the selected parameters.
        - save_memo: Saves the generated memo to a file.

    Note:
        - The function uses various helper functions and classes to process the data and generate visualizations.
        - It assumes the existence of certain file paths and mappings (e.g., communityshape_path, INDICATOR_UNIT_MAPPING).
        - The WriteMemo class is used to generate a memo about the data using an external API (open_ai_key).
    """

    form = SearchForm(request.GET or None)
    subgroup_form = SubgroupForm(year_choices=[])

    if request.method == "GET" and form.is_valid():
        form = SearchForm(request.GET)
        subgroup_form = SubgroupForm(year_choices=[])

    if form.is_valid():
        # Extract variables from SearchForm
        geograpahic_level = form.cleaned_data["geographic_level"]
        category = form.cleaned_data["category"]
        year = form.cleaned_data["year"]
        generate_memo = form.cleaned_data["generate_memo"]

        geographic_level_dct = {
            "City of Chicago": [],
            "Community": form.cleaned_data["community"],
            "Zipcode": form.cleaned_data["zipcode"],
            "Tract": form.cleaned_data["tract"],
        }

        indicator_dct = {
            "Economic": form.cleaned_data["economic_indicators"],
            "Education": form.cleaned_data["education_indicators"],
            "Health": form.cleaned_data["health_indicators"],
            "Housing": form.cleaned_data["housing_indicators"],
            "Population": form.cleaned_data["population_indicators"],
        }

        geographic_unit = geographic_level_dct[geograpahic_level]
        indicator = indicator_dct[category]
        model = MAIN_MODEL_MAPPING[indicator]
        subgroup_model = SUB_MODEL_MAPPING[indicator]

        print("### USER SELECTION ###")
        print("Geographic Level Selected:", geograpahic_level)
        print(geograpahic_level, "Selected:", geographic_unit)
        print("Category Selected:", category)
        print("Indicator Selected:", indicator)
        print("Periods(s) Selected:", year)
        print("Generate Memo:", generate_memo)

        subgroup_form = SubgroupForm(
            year_choices=[
                (str(year), str(year)) for year in form.cleaned_data["year"]
            ]
        )
        # Create main table context variables
        maintable = MainTable(
            geograpahic_level, geographic_unit, indicator, model, year
        )
        field = maintable.table
        table_title = maintable.table_title

        # Create subtable context variables
        subgroup_tables = SubgroupTable(
            geograpahic_level, geographic_unit, indicator, subgroup_model, year
        )

        multi_year_subtable_field = subgroup_tables.many_subtables

        chart_data = prepare_chart_data(field)
        subgroup_chart_data = prepare_subgroup_chart_data(multi_year_subtable_field)

        # Creating heat map for Community Area, Zip Code, and Tract Level
        heatmap_data, heatmap_info = generate_heatmaps(geograpahic_level, indicator, field, year)

        if generate_memo == "Yes":
            # Writing and saving memo about the data
            chart_descr = heatmap_data.describe()
            analysis = WriteMemo(
                indicator, geograpahic_level, field, chart_descr, open_ai_key
            )
            memo = analysis.invoke()
            memo_path = save_memo(indicator, geograpahic_level, memo)

            context = {
                "form": form,
                "field": field,
                "table_title": table_title,
                "multi_year_subtable_field": multi_year_subtable_field,
                "chart_data": chart_data,
                "subgroup_chart_data": subgroup_chart_data,
                "paths_titles": heatmap_info,
                "subgroup_form": subgroup_form,
                "memo": memo,
                "memo_path": memo_path,
            }
            return render(request, "dataandvisualize.html", context)

        else:
            context = {
                "form": form,
                "field": field,
                "table_title": table_title,
                "multi_year_subtable_field": multi_year_subtable_field,
                "chart_data": chart_data,
                "subgroup_chart_data": subgroup_chart_data,
                "paths_titles": heatmap_info,
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
    """
    Renders the resources page of the application.

    This function handles the request for the resources page URL (/main/resources/) and renders the "resources.html" template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered "resources.html" template as an HTTP response.
    """
    return render(request, "resources.html")

# Source: https://stackoverflow.com/questions/19400089/downloadable-docx-file-in-django
def download_memo(request):
    """
    Allows users to download the generated memo.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The downloadable memo or an error if the memo was 
        not found.
    """
    if "memo_path" in request.GET:
        memo_path = request.GET["memo_path"]

        if os.path.exists(memo_path):

            with open(memo_path, "rb") as docx_file:
                response = HttpResponse(
                    docx_file.read(),
                    content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                )
                response[
                    "Content-Disposition"
                ] = 'attachment; filename="memo.docx"'
                return response

    return HttpResponse("Memo not found", status=404)
