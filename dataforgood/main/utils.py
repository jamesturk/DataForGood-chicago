from .models import Georeference, EconomicMain, EconomicSub

# Helps for views.py
def create_table(category, geographic_level, geographic_unit, indicator, year):
    """
    """
    headers = [geographic_level] + list(year)
    rows = []

    model = get_model(category)
            
    for unit in geographic_unit:
        row = [unit]
        results = query_database(model, unit, indicator, year)
        for r in results:
            row.append(r.value)
        rows.append(row)
    
    return {'headers':headers, 'rows':rows}


def query_database(model, unit, indicator, year):
    """
    """
    if len(year) == 1:
        year = (year[0], )
    else:
        year = tuple(year)

    results = model.objects.filter(georeference_id=unit,
                                    indicator_name=indicator,
                                    year__in=year)

    return results

def get_model(category_name):
    """
    """
    category_mapping = {'Economic':EconomicMain}
    return category_mapping[category_name]


# Helpers for models.py
def get_choices(model_name, col):
    """
    """
    choices = []
    unique_values = list(model_name.objects.values(col).distinct())
    for item in unique_values:
        choices.append(tuple([item[col], item[col]]))
    
    return choices