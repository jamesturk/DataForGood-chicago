from django import forms
from django.db.models import Avg

from .models import MedianIncome_Main, MeanIncome_Main, ContractRent_Main, \
    HouseholdType_Main, MedianEarning_Main, Enrollment_Main, Disability_Main, \
    Insurance_Main, Races_Main, MedianAge_Main, MedianIncome_Sub, MeanIncome_Sub, \
    ContractRent_Sub, HouseholdType_Sub, MedianEarning_Sub, Enrollment_Sub, \
    Disability_Sub, Insurance_Sub, Races_Sub, MedianAge_Sub, TractZipCode


# HELPER FUNCTIONS FOR VIEWS.PY #

# Global variables that map form indicator options to specific models to conduct querying
MAIN_MODEL_MAPPING = {
    "Median Income in the Past 12 Months (inflation-adjusted)": MedianIncome_Main,
    "Mean Income in the Past 12 Months (inflation-adjusted)": MeanIncome_Main,
    "Aggregate Contract Rent": ContractRent_Main,
    "Total Number of Households": HouseholdType_Main,
    "Median Earnings in the Past 12 Months": MedianEarning_Main,
    "Population 3 years and over enrolled in school": Enrollment_Main,
    "Total Population With Disability": Disability_Main,
    "Insurance Coverage: Total Population": Insurance_Main,
    "Total Population and Race Group": Races_Main,
    "Median Age": MedianAge_Main,
}

SUB_MODEL_MAPPING = {
    "Median Income in the Past 12 Months (inflation-adjusted)": MedianIncome_Sub,
    "Mean Income in the Past 12 Months (inflation-adjusted)": MeanIncome_Sub,
    "Aggregate Contract Rent": ContractRent_Sub,
    "Total Number of Households": HouseholdType_Sub,
    "Median Earnings in the Past 12 Months": MedianEarning_Sub,
    "Population 3 years and over enrolled in school": Enrollment_Sub,
    "Total Population With Disability": Disability_Sub,
    "Insurance Coverage: Total Population": Insurance_Sub,
    "Total Population and Race Group": Races_Sub,
    "Median Age": MedianAge_Sub,
}

INDICATOR_UNIT_MAPPING = {
    "Median Income in the Past 12 Months (inflation-adjusted)": "US Dollars",
    "Mean Income in the Past 12 Months (inflation-adjusted)": "US Dollars",
    "Aggregate Contract Rent": "US Dollars",
    "Total Number of Households": "Number of Households",
    "Median Earnings in the Past 12 Months": "US Dollars",
    "Population 3 years and over enrolled in school": "Number of People",
    "Total Population With Disability": "Number of People",
    "Insurance Coverage: Total Population": "Number of People",
    "Total Population and Race Group": "Number of People",
    "Median Age": "Years"
}

SUBGROUP_NAMES = {
    "median_white": "White",
    "median_hawai": "Native Hawaiian and Other Pacific Islander",
    "median_asia": "Asian",
    "median_ind_ala": "American Indian and Alaska Native",
    "median_other": "Some Other Race",
    "median_black": "Black",
    "less_high": "Less Than High School Graduate",
    "grad": "Graduate or Professional Degree",
    "high": "High School Graduate",
    "bachelor": "Bachelor's Degree",
    "college": "Some College and Associate's Degree",
    "kind_12": "Kindergarten to 12th Grade",
    "grad": "Graduate or Professional School",
    "college": "College, Undergraduate",
    "nursery": "Nursery School, Preschool",
    "ind_living": "With an Independent Living Difficulty",
    "ambulatory": "With an Ambulatory Difficulty",
    "self_care": "With a Self-Care Difficulty",
    "vision": "With a Vision Difficulty",
    "hearing": "With a Hearing Difficulty",
    "cognitive": "With a Cognitive Difficulty",
    "insured": "Insured",
    "uninsured": "Uninsured",
    "lower_rent": "Lower Contract Rent Quartile",
    "upper_rent": "Upper Contract Rent Quartile",
    "median_rent": "Median Contract Rent",
    "household_family": "Total Number of Family Household",
    "household_nonfamily": "Total Number of Non-family Household",
    "pop_hawai": "Native Hawaiian and  Other Pacific Islander",
    "pop_asia": "Asian",
    "pop_black": "Black",
    "pop_white": "White",
    "pop_two": "Two or More Races",
    "pop_other": "Some Other Race",
    "pop_ind_ala": "American Indian and Alaska Native",
}

def convert_list_to_tuple(query_lst):
    """
    Converts lists of variables (e.g. years or tracts) into tuples to
    run model query for table creation.
    Examples:
        - [2018, 2019] -> (2018, 2019)
        - [2018] -> (2018,)

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


def convert_periods_to_years(periods):
    """
    Takes in the 5-year estimate period(s) selected by the user and retains
    only the ending year of each period selected to conduct query
    An example:
        ['2011-2015', '2016-2020'] -> [2015, 2020]
        ['2011-2015'] -> [2015]

    Inputs:
        period (list of str): 5-year period(s) selected by the user
    
    Returns:
        years (list of int): the ending year for each 5-year estimate period
            selected by the user
    """
    years = []
    for p in periods:
        years.append(int(p[5:]))
    
    return years


def get_subgroups(model_sub):
    """
    Generates a list of unique subgroups for selected geographic units
    for a given indicator.

    Inputs:
        model_sub (Django model): sub model of the indicator selected by user

    Returns:
        subgroups_lst (list of str): a list of unique subgroups
    """
    subgroups = model_sub.objects.values_list("sub_group_indicator_name").distinct()
    subgroups_lst = []
    for subgroup in subgroups:
        subgroups_lst.append(subgroup[0])
    
    return subgroups_lst


def create_table_title(indicator, year):
    """
    Creates a title for the main table based on indicator and year(s) selected
    by the user.

    Inputs:
        indicator (str): indicator selected by the user in the form
        year (list of strs): 5-year periods selected by the user in the form

    Returns:
        indicator_formatted (str): readable indicator format and 5-year periods
            selected by the user
    """
    indicator_formatted = indicator.replace("_", " ").title() + " for "
    
    for year in year:
        indicator_formatted += year + ", "
    
    return indicator_formatted


def convert_none_to_na_and_round(single_result):
    """
    Takes in a query result value returns the result (rounded to 2 decimal
        places) if the query is not None, else return "NA" string
    
    Inputs:
        single_result (int or None): query result value
    
    Returns: "NA" string or query result (int) rounded to 2 decimal places
    """
    if single_result is None:
        return "NA"
    else:
        return round(single_result, 2)


def create_table(geographic_level, geographic_unit, indicator, periods):
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
        periods (list of str): periods(s) selected by the user

    Returns: a dictionary of two items
            - 'headers': header row of table (list of str)
            - 'rows': multiple rows for each geographic unit (list of lists of
                str)
    """
    headers = [geographic_level] + list(periods)
    rows = []

    model = MAIN_MODEL_MAPPING[indicator]

    # Converts list of years to tuple, if only one year selected,
    # converts list to tuple with a comma
    years = convert_list_to_tuple(convert_periods_to_years(periods))

    if geographic_level == "City of Chicago":
        row = ["City Average"]
        results = (
            model.objects.values("year")
            .filter(year__in=years)
            .annotate(Avg("value"))
            .order_by("year")
        )

        for r in results:
            row.append(round(r["value__avg"], 2))
        rows.append(row)

    # Creates a row for each geographic unit
    for unit in geographic_unit:
        row = [unit]

        if geographic_level == "Tract":
            results = model.objects.filter(census_tract_id=unit, year__in=years)

            # Appends value for each year
            for r in results:
                if r.value is None:
                    row.append('NA')
                else:
                    row.append(r.value)

        elif geographic_level == "Zipcode":
            # Obtain tracts in the selected zipcode
            tracts_in_zipcode = list(
                TractZipCode.objects.filter(zip_code=unit)
                .values_list("tract_id")
                .distinct()
            )

            # Groupby year, sorted by year in ascending order and
            # takes the mean of observations
            results = (
                model.objects.values("year")
                .filter(census_tract_id__in=tracts_in_zipcode, year__in=years)
                .annotate(Avg("value"))
                .order_by("year")
            )

            # Appends value for each year
            for r in results:
                #row.append(round(r["value__avg"], 2))
                row.append(convert_none_to_na_and_round(r["value__avg"]))

        elif geographic_level == "Community":
            # Groupby community area and year, sorted by year in ascending order
            # and takes the mean of observations
            results = (
                model.objects.values("census_tract_id__community", "year")
                .filter(census_tract_id__community=unit, year__in=years)
                .annotate(Avg("value"))
                .order_by("year")
            )

            # Appends value for each year
            for r in results:
                row.append(convert_none_to_na_and_round(r["value__avg"]))

        rows.append(row)

    return {"headers": headers, "rows": rows}


def create_subgroup_table_rows(subgroup_lst, rows, results):
    """
    Creates a row for each subgroup based on query results.

    Inputs:
        subgroup_lst (list of str): list of subgroup names
        rows (list of lists): a single list to store each row as a list
        results (Django queryset): a queryset item of dictionaries, each
            dictionary is a query result instance
    
    Returns:
        rows (list of lists): a single list with each subgroup stored as a list
    """
    for subgroup in subgroup_lst:
        row = [SUBGROUP_NAMES[subgroup]]
        for r in results.filter(sub_group_indicator_name=subgroup):
            row.append(convert_none_to_na_and_round(r["value__avg"]))
        rows.append(row)
    
    return rows


def create_subgroup_tables(geographic_level, geographic_unit, indicator, periods):
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
        periods (list of str): periods(s) selected by the user

    Returns: a nested dictionary of dictionaries, each dictionary corresponding
        one year.
        For each year's nested dictionary, there are two items
            - 'headers': header row of table (list of str)
            - 'rows': multiple rows for each geographic unit (list of lists of
                str)
    """
    # Note: Hard coded here for dummy database testing
    model = SUB_MODEL_MAPPING[indicator]

    # Creates a nested dictionary, one dictionary for each year
    table_many_years = {}

    # Obtain list of subgroups
    subgroup_lst = get_subgroups(model)

    # Convert periods to years
    years = convert_list_to_tuple(convert_periods_to_years(periods))

    for period_str, one_year in zip(periods, years):
        headers = [geographic_level] + list(geographic_unit)
        rows = []

        if geographic_level == "City of Chicago":
            results = (
                model.objects.values("sub_group_indicator_name")
                .filter(year=one_year)
                .annotate(Avg("value"))
                .order_by("sub_group_indicator_name")
            )

            rows = create_subgroup_table_rows(subgroup_lst, rows, results)

        if geographic_level == "Tract":
            results = (
                model.objects.filter(
                    census_tract_id__in=geographic_unit, year=one_year
                )
                .values("census_tract_id", "sub_group_indicator_name")
                .annotate(Avg("value"))
                .order_by("sub_group_indicator_name", "census_tract_id")
            )

            rows = create_subgroup_table_rows(subgroup_lst, rows, results)

        if geographic_level == "Zipcode":
            # Create a dictionary to save values for each subgroup
            subgroup_dct = {subgroup: [] for subgroup in subgroup_lst}

            # Conduct querying for each zipcode (joining tract id each time)
            for zipcode in geographic_unit:
                # Obtain tracts in one zipcode
                tracts_in_zipcode = list(
                    TractZipCode.objects.filter(zip_code=zipcode)
                    .values_list("tract_id")
                    .distinct()
                )

                # Obtain subgroup averages for one zipcode
                results = (
                    model.objects.filter(
                        census_tract_id__in=tracts_in_zipcode, year=one_year
                    )
                    .values("sub_group_indicator_name")
                    .annotate(Avg("value"))
                    .order_by("sub_group_indicator_name")
                )
 
                # Append results to subgroup dictionary
                for r in results:
                    subgroup_dct[r["sub_group_indicator_name"]].append(
                        convert_none_to_na_and_round(r["value__avg"]))

            # Convert dictionary values to list of lists for table
            rows = [[SUBGROUP_NAMES[subgroup]] + row for subgroup, 
                    row in subgroup_dct.items()]

        if geographic_level == "Community":
            results = (
                model.objects.filter(
                    census_tract_id__community__in=geographic_unit,
                    year=one_year,
                )
                .values(
                    "census_tract_id__community", "sub_group_indicator_name"
                )
                .annotate(Avg("value"))
                .order_by(
                    "sub_group_indicator_name", "census_tract_id__community"
                )
            )

            rows = create_subgroup_table_rows(subgroup_lst, rows, results)

        table_many_years[period_str] = {"headers": headers, "rows": rows}

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


def create_multiple_choice_geo(
    model, field_name, widget_id, class_name="form-option"
):
    """
    Create a dynamically configured MultipleChoiceField based on the specified model and field.

    :param model: Django model class from which to fetch choices.
    :param field_name: Name of the model field for which to create a choice field.
    :param widget_id: HTML ID to use for the field's widget.
    :param class_name: CSS class name for the widget.
    :return: forms.MultipleChoiceField instance.
    """
    return forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(
            attrs={"class": class_name, "id": widget_id}
        ),
        choices=get_choices(model, field_name),
    )


def create_multiple_choice_indicator(
    choices_lst, widget_id, class_name="form-option"
):
    """
    Create a dynamically configured MultipleChoiceField based on the specified model and field.

    :param model: Django model class from which to fetch choices.
    :param field_name: Name of the model field for which to create a choice field.
    :param widget_id: HTML ID to use for the field's widget.
    :param class_name: CSS class name for the widget.
    :return: forms.MultipleChoiceField instance.
    """
    return forms.ChoiceField(
        widget=forms.Select(attrs={"class": class_name, "id": widget_id}),
        choices=choices_lst,
    )
