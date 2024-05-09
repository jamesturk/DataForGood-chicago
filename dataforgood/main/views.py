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
                category, geograpahic_level, geographic_unit, indicator, year
            )

            # Create subtable context variables
            multi_year_subtable_field = create_subgroup_tables(
                category, geograpahic_level, geographic_unit, indicator, year
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

            heatmap = None
            
            if geograpahic_level != 'City of Chicago':
                heatmap_data = pd.DataFrame(field["rows"], columns=field["headers"])
                heatmap_data['value'] = heatmap_data.iloc[:, 1:].sum(axis=1)
                heatmap_data = heatmap_data.iloc[:, [0, -1]]

                if geograpahic_level == "Community Area":
                    geo = gpd.read_file(communityshape_path)
                    data = pd.merge(geo, heatmap_data, left_on='community', 
                                    right_on='Community Area')
                    
                if geograpahic_level == "Zipcode":
                    geo = gpd.read_file(zipcodeshape_path)
                    geo['zip'] = geo['zip'].astype(int)
                    data = pd.merge(geo, heatmap_data, left_on='zip', 
                                    right_on='Zipcode')
                    
                if geograpahic_level == "Tract":
                    geo = gpd.read_file(censusshape_path)
                    data = pd.merge(geo, heatmap_data, left_on='tractce10', 
                                    right_on='Tract')

                fig, ax = plt.subplots(1, 1, figsize=(15, 9))
                geo.plot(ax=ax, color='lightgray', edgecolor='black', linewidth=0.1)
                data.plot(column='value', ax=ax, cmap='OrRd', legend=True,
                            edgecolor='black', linewidth=0.1)
                buffer = BytesIO()
                plt.savefig(buffer, format='png')
                buffer.seek(0)
                heatmap = base64.b64encode(buffer.read()).decode('utf-8')

            context = {
                "field": field,
                "table_title": table_title,
                "multi_year_subtable_field": multi_year_subtable_field,
                "chart_data": chart_data,
                'heatmap_message': 'A heatmap will generate for the Community Area, Zipcode, and Tract geographic levels.',
                "heatmap": heatmap,
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
