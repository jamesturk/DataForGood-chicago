## Endpoint Documentation
### Endpoint A: /main/aboutus
Purpose: This endpoint provides information about the project behind the web application. It serves as an "About Us" page to give users a better understanding of who is responsible for the application and its purpose.

Parameters: None

Response: HTML page containing the following components:
- Logo and Project Name
- Navigation Bar: “About Us”, “Data & Visualize”, and “Resource”
- Project Description and Objectives
- A button leading to the “Data & Visualize” page

Template Context Variables:
- `project_name`: The name of the company or organization
- `project_description`: A brief description of the project's mission or objectives
- `“Explore Data”` Button: A button leading to the endpoint B: /main/data&visualize
### Endpoint B: /main/data&visualize
Purpose: This endpoint serves as the main page for the "Data & Visualize" tab, allowing users to select parameters and view visualizations of the data. Users have to go through url B1, B2, B3, B4, and B5 in consecutive order to successfully initiate a query to generate the relevant data tables and charts to be displayed on the HTML page.

Parameters
- `geographic_level`: The geographic level to display data for. Valid values are "City of Chicago" or  “Community” or "Zipcode" or “Tract”. One selection at a time. Defaults to "City of Chicago" if not provided.
- `geographic_unit`: Depending on the geographic level selected, the options change to display geographic unit variables available in the database for the corresponding geographic level. Multi-checkbox selection for “Community” or "Zipcode" or “Tract” levels, no selections available for "City of Chicago" level. Defaults to "Albany Park" for "Community" level; defaults to "60601" for "Zipcode" level; defaults to "10100" for "Tract" level.
- `indicator_category`: The category of indicators available to select. Valid values are  "Economic", "Education", "Health", "Housing", "Population".
- `indicator_variable`: Depending on the indicator category selected, the options change to display the indicators available for the selected category. One selection at a time. Defaults to "Median Income in the Past 12 Months" for "Economic" category; defaults to "Median Earnings in the Past 12 Months" for "Education" category; defaults to "Total Population With Disability" for "Health" category; defaults to "Aggregate Contract Rent" for Housing category; defaults to "Total Population and Race Group" for "Housing" category.
- `year`: a list of five-year periods to include in the data tables and visualizations. Valid values are "2013-2017", "2014-2018", "2015-2019", "2016-2020", "2017-2021", "2018-2022". Multi-checkbox selection. Defaults to "2013-2017".
- `generate_memo`: Determines if a ChatGPT analytical memo will be generated on the webapp along with the data tables and visualizations. Valid values are "Yes: and "No". Defaults to "No".

##### Example HTML Links
- Example 1:
  `/main/data&visualize/?csrfmiddlewaretoken=<token_number>&geographic_level=Community&tract=<default_tract>&zipcode=<default_tract>&community=HYDE+PARK&category=Economic&economic_indicators=Median+Income+in+the+Past+12+Months+inflation-adjusted&education_indicators=Median+Earnings+in+the+Past+12+Months&health_indicators=<default_health_indicator>&housing_indicators=<default_housing_indicator>&population_indicators=<default_population_indicator>&year=2013-2017&year=2014-2018&generate_memo=No`
  - `geographic_level`: Community - Hyde Park
  - `indicator_category`: Economic
  - `indicator_variable`: Median Income in the Past 12 Months
  - `years`: 2013-2017, 2014-2018 (*multiple five-year estimates*)
  - 'generate_memo': No
- Example 2:
  `/main/data&visualize/?csrfmiddlewaretoken=<token_number>&geographic_level=Community&tract=<default_tract>&zipcode=<default_tract>&community=HYDE+PARK&category=Education&economic_indicators=<default_economic_indicator>&education_indicators=Population+3+years+and+over+enrolled+in+school&health_indicators=<default_health_indicator>&housing_indicators=<default_housing_indicator>&population_indicators=<default_population_indicator>&year=2018-2022&generate_memo=No`
  - `geographic_level`: Community - Hyde Park
  - `indicator_category`: Education
  - `indicator_variable`: Population 3 years and over enrolled in school
  - `years`: 2018-2022 (*single five-year estimate*)
  - `generate_memo`: No
- Example 3:
  `/main/data&visualize/?csrfmiddlewaretoken=<token_number>&geographic_level=Community&tract=<default_tract>&zipcode=<default_tract>&community=HYDE+PARK&community=LINCOLN+PARK&category=Education&economic_indicators=<default_economic_indicator>&education_indicators=Population+3+years+and+over+enrolled+in+school&health_indicators=<default_health_indicator>&housing_indicators=<default_housing_indicator>&population_indicators=<default_population_indicator>&year=2018-2022&generate_memo=Yes`
  - `geographic_level`: Community - Hyde Park, Lincoln Park (multiple community areas)
  - `indicator_category`: Education
  - `indicator_variable`: Population 3 years and over enrolled in school
  - `years`: 2018-22 (*single five-year estimate*)
  - `generate_memo`: Yes
- Example 4:
  `/main/data&visualize/?csrfmiddlewaretoken=<token_number>&geographic_level=Zipcode&tract=<default_tract>&zipcode=60610&zipcode=60611&zipcode=60612&community=<default_community>&category=Education&economic_indicators=<default_economic_indicator>&education_indicators=Population+3+years+and+over+enrolled+in+school&health_indicators=<default_health_indicator>&housing_indicators=<default_housing_indicator>&population_indicators=<default_population_indicator>&year=2018-2022&generate_memo=Yes`
  - `geographic_level`: Zipcode - 60610, 60611, 60612 (multiple zipcodes)
  - `indicator_category`: Education
  - `indicator_variable`: Population 3 years and over enrolled in school
  - `years`: 2018-22 (*one five-year estimate*)
  - `generate_memo`: Yes
    
 ##### Response: HTML page with the following components
- Dropdown menus for selecting `geographic_level`, `indicator_category`, `years`, and `indicator_variables`.
- Checkboxes for selecting specific zip codes (if `geographic_level` is "Zip Code").
- Checkboxes for selecting specific community areas (if `geographic_level` is "Community Areas").
- Data tables for the selected data (presumably two data tables), and one for the yearly indicator and another for the subgroup
- 2~ 4 visualizations of the selected data, for example:
  - Bar or line chart of *total population* (indicator) per selected geographic level for the selected years
  - Bar chart of *race group* (sub-indicator) per selected geographic level for the select years
  - More types of visuals may be added
- Buttons to export the dataset in Excel and PDF formats.
- Button to download each of the visualizations we generated based on selected data
- Button to generate memo based on the current view of data tables and data visualizations
- *(optional) Button to make edits on each of the visualizations we generated (mainly for change theme colors or font and text editing)*

 ##### Template Context Variables
- `geographic_level`: The selected geographic level ("City of Chicago" / "Zip Code" / “Community Areas”)
- `indicator_category`: The selected indicator category
- `years`: List of selected years (5-yearly estimates OR yearly estimates depending on indicator selected)
  - *E.g. for **Economic and Housing** indicators (yearly estimates are possible, so the user can select **multiple** years as a checkbox)*
    - 2014
    - 2015
    - 2016
    - 2017
    - 2018
  - *E.g. for the **other categories’** indicators (only 5-year estimates are possible, so the user is only able to select **one** given period)*
    - 2014-2018
    - 2015-2019
    - 2016-2020
    - 2017-2021
    - 2018-2022
- `community_areas`: List of selected community areas (if `geographic_level` is "Community Areas")
- `zip_codes`: List of selected zip codes (if `geographic_level` is "Zip Code")
- `census_tracts`: List of census tracts (if `geographic_level` is Census Tract")
- `indicator_variable` List of available indicator variables. Select one at a time.
- `data_table_indicator_general`: Data table for selected indicator
- `data_table_indicator_sub`: Data table for all sub-indicators
- `data_visualization_general`: Visualization for the selected indicator, geographic level, and years (if multiple years selected)
- `data_visualization_sub_indicator`: Visualization for all sub-indicators of the selected indicator, geographic level, and year
- `year_dropdown_sub_indicator`: a dropdown menu that allows users to select one year at a time for the sub-indicator visualization. The year dictionary here will be a list of user selected years. The default year used is the latest year available or the latest 5-year estimate

#### Endpoint B1:  /main/data&visualize/{parameters from query}/tables.xlsx
Purpose: Enable the user to download the datatables as one .xlsx file, with each datatable as an excel worksheet tab.

Parameters: None

Template variables:
- `href`: HTML link of the exported tables.xlsx file

Reponse: HTML page that exports that datatable (from a .json or pandas dataframe) as a .xlsx file.

#### Endpoint B2:  /main/data&visualize/{parameters from query}/tables.pdf
Purpose: Enable the user to download the datatables as a .pdf file, with each datatable as a page in the PDF document.

Parameters: None

Template variables:
- `href`: HTML link of the exported tables.pdf file

Reponse: HTML page that exports that datatable (from a .json or pandas dataframe) as a .pdf file.

#### Endpoint B3:  /main/data&visualize/{parameters from query}/chart_1.jpg
Purpose: There will be one unique link for each chart in the HTML page. This enables the user to select the specific charts to download as a .jpg image, with each image being one chart.

Parameters: None

Template variables:
- `href`: HTML link of the exported chart_1.jpg file

Reponse: HTML page that exports the chart as a .jpg file.

### Endpoint C: /main/resources
Purpose: This endpoint provides a view of an embedded ArcGIS web app.

Parameters: None/NA

Response: HTML page with the embedded ArcGIS web app which contains a lot of feature layers to interact with.

### Endpoint D: /main/download-memo/

Purpose: Allows users to download the generated memo from our web app.

Parameters: None/NA

Parameters:
- `request` (HttpRequest): The HTTP request object containing information about the request.

Response:
- `HttpResponse`: The response is either the downloadable memo or an error message if the memo was not found.

