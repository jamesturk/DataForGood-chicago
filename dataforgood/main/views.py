import os
import uuid

import environ
import folium
import geopandas as gpd
import numpy as np
import pandas as pd
from django.shortcuts import render
from django.template.defaulttags import register
from django.views.decorators.csrf import csrf_protect

from dataforgood.settings import BASE_DIR

from .forms import SearchForm, SubgroupForm
from .utils import (
    INDICATOR_UNIT_MAPPING,
    WriteMemo,
    create_subgroup_tables,
    create_table,
    create_table_title,
    save_memo,
)


communityshape_path = os.path.join(BASE_DIR, "main/communityarea")
zipcodeshape_path = os.path.join(BASE_DIR, "main/zipcode")
censusshape_path = os.path.join(BASE_DIR, "main/censustracts")
html_path = os.path.join(BASE_DIR, "main/templates/maps")
docs_path = os.path.join(BASE_DIR, "main/templates/memos")

env = environ.Env()
environ.Env.read_env()
open_ai_key = env("open_ai_key")

# Centroid of Chicago for heat map
y_center = 41.434732
x_center = -87.333050


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
@csrf_protect
def dataandvisualize(request):
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
        table_title = create_table_title(indicator, year)
        field = create_table(
            geograpahic_level, geographic_unit, indicator, year
        )

        # Create subtable context variables
        multi_year_subtable_field = create_subgroup_tables(
            geograpahic_level, geographic_unit, indicator, year
        )

        # print("### MAIN TABLE ###")
        # print("Header:", field["headers"])
        # print("Rows:", field["rows"])

        # print("### SUBGROUP TABLES DICTIONARY ###")
        # for year, dct in multi_year_subtable_field.items():
        #     print(year, dct)
        # Prepare data for the main chart
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

        # Prepare data for the subgroup chart
        subgroup_chart_data = {}
        for year_value, subtable_data in multi_year_subtable_field.items():
            subgroup_chart_data[year_value] = {
                "categories": subtable_data["headers"][
                    1:
                ],  # Subgroup categories
                "series": [
                    {
                        "name": subtable_data["headers"][0],
                        "data": [
                            row[1:] for row in subtable_data["rows"]
                        ],  # Subgroup values
                    }
                ],
            }

        # Creating heat map for Community Area, Zip Code, and Tract Level
        heatmap_data = pd.DataFrame(field["rows"], columns=field["headers"])
        heatmap_info = []

        years = heatmap_data.columns[1:]
        for year in years:
            year_dic = {}
            for column in heatmap_data.columns[1:]:
                heatmap_data[column] = heatmap_data[column].apply(
                    lambda x: float(x) if x != "NA" else np.nan
                )

            if geograpahic_level != "City of Chicago":
                if geograpahic_level == "Community":
                    heatmap_data.iloc[:, 0] = heatmap_data.iloc[
                        :, 0
                    ].str.upper()
                    geo = gpd.read_file(communityshape_path)
                    data = pd.merge(
                        geo,
                        heatmap_data,
                        left_on="community",
                        right_on="Community",
                    )

                if geograpahic_level == "Zipcode":
                    geo = gpd.read_file(zipcodeshape_path)
                    data = pd.merge(
                        geo, heatmap_data, left_on="zip", right_on="Zipcode"
                    )

                if geograpahic_level == "Tract":
                    geo = gpd.read_file(censusshape_path)
                    data = pd.merge(
                        geo, heatmap_data, left_on="tractce10", right_on="Tract"
                    )

                # Adding base layer
                mymap = folium.Map(
                    location=[y_center, x_center], zoom_start=10, tiles=None
                )
                folium.TileLayer(
                    "CartoDB positron", name="Light Map", control=False
                ).add_to(mymap)

                # Creating heatmap layer
                units = INDICATOR_UNIT_MAPPING[indicator]
                folium.Choropleth(
                    geo_data=data,
                    name="Choropleth",
                    data=data,
                    columns=[geograpahic_level, year],
                    key_on="feature.properties.{}".format(geograpahic_level),
                    fill_color="YlGnBu",
                    fill_opacity=1,
                    line_opacity=0.2,
                    bins=3,
                    legend_name=units,
                    smooth_factor=0,
                    nan_fill_color="grey",
                    nan_fill_opacity=0.4,
                ).add_to(mymap)

                def style_function(x):
                    return {
                        "fillColor": "#ffffff",
                        "color": "#000000",
                        "fillOpacity": 0.1,
                        "weight": 0.1,
                    }

                def highlight_function(x):
                    return {
                        "fillColor": "#000000",
                        "color": "#000000",
                        "fillOpacity": 0.5,
                        "weight": 0.1,
                    }

                # Adding tooltips to map
                feat = folium.features.GeoJson(
                    data,
                    style_function=style_function,
                    control=False,
                    highlight_function=highlight_function,
                    tooltip=folium.features.GeoJsonTooltip(
                        fields=[geograpahic_level, year],
                        aliases=[geograpahic_level, units],
                        style=(
                            "background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"
                        ),
                    ),
                )
                mymap.add_child(feat)
                mymap.keep_in_front(feat)
                folium.LayerControl().add_to(mymap)
                if geograpahic_level[-1:] == "y":
                    title = "Heat Map of {} by Selected {}ies in {}".format(
                        indicator, geograpahic_level[:-1], year
                    )
                else:
                    title = "Heat Map of {} by Selected {}s in {}".format(
                        indicator, geograpahic_level, year
                    )

                name = "heatmap_{}".format(uuid.uuid4())
                map_file_path = "{}/{}.html".format(html_path, name)
                mymap.save(map_file_path)
                year_dic["title"] = title
                year_dic["path"] = "maps/{}.html".format(name)
                year_dic["year"] = year
                heatmap_info.append(year_dic)

        if generate_memo == "Yes":
            # Writing and saving memo about the data
            chart_descr = heatmap_data.describe()
            analysis = WriteMemo(
                indicator, geograpahic_level, field, chart_descr, open_ai_key
            )
            memo = analysis.invoke()
            memo_path = save_memo(indicator, geograpahic_level, memo, docs_path)

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
    return render(request, "resources.html")
