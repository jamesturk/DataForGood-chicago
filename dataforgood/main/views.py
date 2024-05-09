from django.shortcuts import render, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import Context, loader
from django.template.defaulttags import register

from .utils import create_table, create_subgroup_tables, create_table_title
from .models import Georeference, EconomicMain, EconomicSub
from .forms import SearchForm

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


# Main Page - /main/
def index(request):
    return render(request, 'index.html')


# About Us Page - /main/about_us/
def aboutus(request):
    return render(request, 'aboutus.html')


# Data and Visualize with FORMS - /main/data&visualize/
def dataandvisualize(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            # Extract variables from SearchForm
            geograpahic_level = form.cleaned_data['geographic_level']
            geographic_unit = form.cleaned_data['tract']
            category = form.cleaned_data['category']
            indicator = form.cleaned_data['indicator']
            year = form.cleaned_data['year']

            # Create main table context variables
            table_title = create_table_title(indicator, year)
            field = create_table(category, geograpahic_level, geographic_unit, indicator, year)

            # Create subtable context variables
            multi_year_subtable_field = create_subgroup_tables(category, geograpahic_level, geographic_unit, indicator, year)
            print(multi_year_subtable_field)

            # Hardcoding subtable title for testing
            subtable_year = str(year[0])

            # Prepare data for the chart
            chart_data = {
                'categories': field['headers'][1:],  # Years
                'series': []
            }
            for row in field['rows']:
                chart_data['series'].append({
                    'name': row[0],  # Geographic unit
                    'data': row[1:]  # Values for each year
                })

            context = {
                'field': field,
                'table_title': table_title,
                'subtable_field': multi_year_subtable_field[subtable_year],
                'subtable_year': subtable_year,
                'chart_data': chart_data
            }
            return render(request, "dataandvisualize.html", context)

    return render(request, "dataandvisualize.html", {'form': form})


# Resources Page - /main/resources/
def resources(request):
    return render(request, "resources.html")