from .models import *
from django import forms
from django.db.models import Avg, Sum

# HELPER FUNCTIONS FOR VIEWS.PY #


# Global variables that map form indicator options to specific models to conduct querying
MAIN_MODEL_MAPPING = {"Median Income in the Past 12 Months (inflation-adjusted)" : MedianIncome_Main,
                      "Mean Income in the Past 12 Months (inflation-adjusted)" : MeanIncome_Main,
                      "Aggregate Contract Rent" : ContractRent_Main,
                      "Total Number of Households" : HouseholdType_Main,
                      "Median Earnings in the Past 12 Months" : MedianEarning_Main,
                      "Population 3 years and over enrolled in school" : Enrollment_Main,
                      "Total Population With Disability" : Disability_Main,
                      "Insurance Coverage: Total Population" : Insurance_Main,
                      "Total Population and Race Group" : Races_Main,
                      "Median Age" : MedianAge_Main}

SUB_MODEL_MAPPING = {"Median Income in the Past 12 Months (inflation-adjusted)" : MedianIncome_Sub,
                      "Mean Income in the Past 12 Months (inflation-adjusted)" : MeanIncome_Sub,
                      "Aggregate Contract Rent" : ContractRent_Sub,
                      "Total Number of Households" : HouseholdType_Sub,
                      "Median Earnings in the Past 12 Months" : MedianEarning_Sub,
                      "Population 3 years and over enrolled in school" : Enrollment_Sub,
                      "Total Population With Disability" : Disability_Sub,
                      "Insurance Coverage: Total Population" : Insurance_Sub,
                      "Total Population and Race Group" : Races_Sub,
                      "Median Age" : MedianAge_Sub}


def convert_list_to_tuple(query_lst):
    """
    Converts lists of variables (e.g. years or tracts) into tuples to
    run model query for table creation.
    An example:
        [2018, 2019] -> (2018, 2019)
        [2018] -> (2018,)

    Inputs:
        query_lst (list): list of query variable(s)

    Returns:
        query_tup (tuple): tuple of query variable(s)
    """
    if len(query_lst) == 1:
        query_tup = (query_lst[0],)
    else:
        query_tup = tuple(query_lst)

    return query_tup


def get_model(indicator, table_type):
    """
    Retrieves model object based on category selected by the user.

    Inputs:
        indicator (str): indicator selected by user in the form
        table_type (str): 'main' for main indicator, 'sub' for subgroup tables

    Returns:
        model (model object): model corresponding to category and indicator
            selected by the user
    """
    if table_type == "main":
        return MAIN_MODEL_MAPPING[indicator]

    if table_type == "sub":
        return SUB_MODEL_MAPPING[indicator]


def get_subgroups(results):
    """
    Generates a list of unique subgroups for selected geographic units
    for a given indicator.

    Inputs:
        results (queryset): a list of query results

    Returns:
        subgroups_lst (list of str): a list of unique subgroups
    """
    subgroups_lst = []
    for tup in results.values_list("sub_group_indicator_name").distinct():
        subgroups_lst.append(tup[0])

    return subgroups_lst


def create_table_title(indicator, year):
    """
    Creates a title for the main table based on indicator and year(s) selected
    by the user.

    Inputs:
        indicator (str): indicator selected by the user in the form
        year (list of int): year(s) selected by the user in the form

    Returns: generated title of main table (str)
    """
    indicator_word_lst = indicator.split("_")
    for idx, word in enumerate(indicator_word_lst):
        indicator_word_lst[idx] = word.capitalize()

    if len(year) == 1:
        year_text = "({year})"
        indicator_word_lst.append(year_text.format(year=str(year[0])))
    else:
        year_range_text = "({start_year}-{end_year})"
        indicator_word_lst.append(
            year_range_text.format(
                start_year=str(year[0]), end_year=str(year[-1])
            )
        )

    return " ".join(indicator_word_lst)

# MODIFIED
def create_table(geographic_level, geographic_unit, indicator, year):
    """
    Generates a dictionary to be used a context variables in the html file to
    create a table on the webapp (for the main indicator/overall group).

    Inputs:
        category: (str): category selected by user in the form
        geographic_level (list of str): geographic level selected by the user
            in the form
        geographic_unit (list of str or int): geographic unit(s) corresponding
            to the geographic level selected by the user in the form
        indicator (str): name of indicator selected by the user in the form
        year (list of int): year(s) selected by the user

    Returns: a dictionary of two items
            - 'headers': header row of table (list of str)
            - 'rows': multiple rows for each geographic unit (list of lists of
                str)
    """
    headers = [geographic_level] + list(year)
    rows = []

    model = get_model(indicator, "main")

    # Converts list of years to tuple, if only one year selected,
    # converts list to tuple with a comma
    year = convert_list_to_tuple(year)

    # Creates a row for each geographic unit
    for unit in geographic_unit:
        row = [unit]
        
        if geographic_level == 'Tract': # AMENDED 11 MAY
            results = model.objects.filter(
            census_tract_id=unit, year__in=year
            )
            for r in results:
                row.append(round(r.value), 2)
        
        # ADDED 11 MAY
        elif geographic_level == 'Zipcode':
            
            # Obtain tracts in the selected zipcode
            tracts_in_zipcode = list(TractZipCode.objects.filter(zip_code=unit).values_list('tract_id').distinct())

            # Groupby year, sorted by year in ascending order and
            # takes the mean of observations
            results = model.objects.values('year').filter(
                census_tract_id__in=tracts_in_zipcode, 
                year__in=year).annotate(Avg('value')).order_by('year')
    
            for r in results:
                row.append(round(r['value__avg'], 2))
        
        # ADDED 11 MAY
        elif geographic_level == 'Community':
            
            # Groupby community area and year, sorted by year in ascending order 
            # and takes the mean of observations
            results = model.objects.values(
                    'census_tract_id__community',
                    'year').filter(census_tract_id__community=unit,
                                   year__in=year).annotate(Avg('value')
                    ).order_by('year')

            for r in results:
                row.append(round(r['value__avg'], 2))
    
        rows.append(row)

    return {"headers": headers, "rows": rows}

# CHANGE THIS SHOULD NOT BE CATEGORY BUT INDICATOR NAME
def create_subgroup_tables(
    geographic_level, geographic_unit, indicator, year
):
    """
    Generates a dictionary to be used a context variables in the html file to
    create a table on the webapp (for the subgroups).

    Inputs:
        category: (str): category selected by user in the form
        geographic_level (list of str): geographic level selected by the user in
            the form
        geographic_unit (list of str or int): geographic unit(s) corresponding
            to the geographic level selected by the user in the form
        indicator (str): name of indicator selected by the user in the form
        year (list of int): year(s) selected by the user

    Returns: a nested dictionary of dictionaries, each dictionary corresponding
        one year.
        For each year's nested dictionary, there are two items
            - 'headers': header row of table (list of str)
            - 'rows': multiple rows for each geographic unit (list of lists of
                str)
    """
    # Retrieve model based on category selected by user (subgroups)
    model = MAIN_MODEL_MAPPING[indicator]
    # Note: Hard coded here for dummy database testing
    model = ContractRent_Sub

    # Creates a nested dictionary, one dictionary for each year
    table_many_years = {}
    for one_year in year:
        headers = [geographic_level] + list(geographic_unit)
        rows = []

        # Converts list of geographic units to tuple, if only one unit selected,
        # converts list to tuple with a comma
        geographic_unit = convert_list_to_tuple(geographic_unit)
        results = model.objects.filter(
            census_tract_id__in=geographic_unit,
            year=one_year,
        )

        # Generates a list of unique subgroups for selected geographic units
        subgroups_lst = get_subgroups(results)

        # Creates a row for each subgroup
        for subgroup in subgroups_lst:
            row = [subgroup.capitalize()]

            # Runs a for loop on each geographic unit to ensure that NAs or
            # empty queries are accounted for (e.g. if a zipcode does not have
            # a subgroup that other zipcodes in the query has)
            for unit in geographic_unit:
                result = model.objects.filter(
                    census_tract_id=unit,
                    sub_group_indicator_name=subgroup,
                    year=one_year,
                )
                if len(result) > 0:
                    row.append(result[0].value)
                else:
                    row.append("NA")
            rows.append(row)

        table_many_years[one_year] = {"headers": headers, "rows": rows}

    return table_many_years


def create_subgroup_tables(geographic_level, geographic_unit, indicator, year):
    """
    Generates a dictionary to be used a context variables in the html file to
    create a table on the webapp (for the subgroups).

    Inputs:
        category: (str): category selected by user in the form
        geographic_level (list of str): geographic level selected by the user in
            the form
        geographic_unit (list of str or int): geographic unit(s) corresponding
            to the geographic level selected by the user in the form
        indicator (str): name of indicator selected by the user in the form
        year (list of int): year(s) selected by the user

    Returns: a nested dictionary of dictionaries, each dictionary corresponding
        one year.
        For each year's nested dictionary, there are two items
            - 'headers': header row of table (list of str)
            - 'rows': multiple rows for each geographic unit (list of lists of
                str)
    """
    # Note: Hard coded here for dummy database testing
    model = EconomicSub

    # Creates a nested dictionary, one dictionary for each year
    table_many_years = {}
    for one_year in year:
        headers = [geographic_level] + list(geographic_unit)
        rows = []

        # Converts list of geographic units to tuple, if only one unit selected,
        # converts list to tuple with a comma
        geographic_unit = convert_list_to_tuple(geographic_unit)

        # AMENDED 11 MAY - Subgroups at Tract level
        if geographic_level == 'Tract':
            results = model.objects.filter(
                georeference_id__in=geographic_unit,
                year=one_year,
            )
        
        # AMENDED 11 MAY - Subgroups at Zipcode level
        elif geographic_level == 'Zipcode':
            results = model.objects.filter(
                georeference_id__zip_code__in=geographic_unit,
                year=one_year,
            )
        
        # AMENDED 11 MAY - Subgroups at Community level
        elif geographic_level == 'Community':
            results = model.objects.filter(
                georeference_id__community_name__in=geographic_unit,
                year=one_year,
            )

        # Generates a list of unique subgroups for selected geographic units
        subgroups_lst = get_subgroups(results)

        # Creates a row for each subgroup
        for subgroup in subgroups_lst:
            row = [subgroup.capitalize()]

            if geographic_level == 'Tract': # AMENDED 11 MAY
                # Runs a for loop on each geographic unit to ensure that NAs or
                # empty queries are accounted for (e.g. if a zipcode does not have
                # a subgroup that other zipcodes in the query has)
                for unit in geographic_unit:
                    result = model.objects.filter(
                        georeference_id=unit,
                        subgroup_indicator_name=subgroup,
                        year=one_year,
                    )
                    if len(result) > 0:
                        row.append(result[0].value)
                    else:
                        row.append("NA")
            
            elif geographic_level == 'Zipcode':
                # Runs a for loop on each geographic unit to ensure that NAs or
                # empty queries are accounted for (e.g. if a zipcode does not have
                # a subgroup that other zipcodes in the query has)
                for unit in geographic_unit:
                    result = model.objects.values(
                        'georeference_id__zip_code').filter(
                            georeference_id__zip_code=unit,
                            subgroup_indicator_name=subgroup,
                            year=one_year, 
                        ).annotate(Avg('value'))
                    if len(result) > 0:
                        row.append(result[0]['value__avg'])
                    else:
                        row.append("NA") 

            elif geographic_level == 'Community':
                # Runs a for loop on each geographic unit to ensure that NAs or
                # empty queries are accounted for (e.g. if a zipcode does not have
                # a subgroup that other zipcodes in the query has)
                for unit in geographic_unit:
                    result = model.objects.values(
                        'georeference_id__community_name').filter(
                            georeference_id__community_name=unit,
                            subgroup_indicator_name=subgroup,
                            year=one_year,
                        ).annotate(Avg('value'))
                    if len(result) > 0:
                        row.append(result[0]['value__avg'])
                    else:
                        row.append("NA")
            
            rows.append(row)

        table_many_years[one_year] = {"headers": headers, "rows": rows}

    return table_many_years

# HELPER FUNCTIONS FOR FORMS.PY #


def get_choices(model, col):
    """
    Generates a list of unique select options based on data in a column of a
        selected model.

    Inputs:
        model (model object): model based on the category selected by the user
        col (str): name of column in the model

    Returns:
        choices (list of tuples): corresponding choices as a list to be used in
            the user search form
    """
    choices = []
    unique_values = list(model.objects.values(col).distinct())
    for item in unique_values:
        choices.append((item[col], item[col]))

    return sorted(choices)

def create_multiple_choice_geo(model, field_name, widget_id, class_name='form-option'):
    """
    Create a dynamically configured MultipleChoiceField based on the specified model and field.
    
    :param model: Django model class from which to fetch choices.
    :param field_name: Name of the model field for which to create a choice field.
    :param widget_id: HTML ID to use for the field's widget.
    :param class_name: CSS class name for the widget.
    :return: forms.MultipleChoiceField instance.
    """
    return forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={'class': class_name, 'id': widget_id}),
        choices=get_choices(model, field_name),
    )

def create_multiple_choice_indicator(choices_lst, widget_id, class_name='form-option'):
    """
    Create a dynamically configured MultipleChoiceField based on the specified model and field.
    
    :param model: Django model class from which to fetch choices.
    :param field_name: Name of the model field for which to create a choice field.
    :param widget_id: HTML ID to use for the field's widget.
    :param class_name: CSS class name for the widget.
    :return: forms.MultipleChoiceField instance.
    """
    return forms.ChoiceField(
        widget=forms.Select(attrs={'class': class_name, 'id': widget_id}),
        choices=choices_lst
    )
