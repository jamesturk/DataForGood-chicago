## Architecture Documentation
Welcome to the DataForGood Chicago project! This document will provide you with an overview of our application's architecture and key concepts to help you get started.

### Data Flow and Backend:
- Data Source: The data for our application comes mainly from the American Community Survey conducted by the Census Bureau. We have a backend database using PostgreSQL, which stores this data in a structured format. The following is a table view of the indicators we have for each category:
- Time Unit:
* 2013-2017 ACS 5-year estimate
* 2014-2018 ACS 5-year estimate
* 2015-2019 ACS 5-year estimate
* 2016-2020 ACS 5-year estimate
* 2017-2021 ACS 5-year estimate
* 2018-2022 ACS 5-year estimate

| Category | Description | Variable Name | Units | Variable Code 
|----------|-------------|---------------|-------|---------------
| Economics | Median Income in the Past 12 Months (inflation-adjusted) by race | Median Income in the Past 12 Months (inflation-adjusted) | dollars | S1903_C03_001E 
| Economics | Median Income in the Past 12 Months (inflation-adjusted) by race | By race: white | dollars | S1903_C03_002E 
| Economics | Median Income in the Past 12 Months (inflation-adjusted) by race | By race: black or african american | dollars | S1903_C03_003E 
| Economics | Median Income in the Past 12 Months (inflation-adjusted) by race | By race: american indian and alaska native | dollars | S1903_C03_004E 
| Economics | Median Income in the Past 12 Months (inflation-adjusted) by race | By race: asian | dollars | S1903_C03_005E | 5-year estimate: 2017-2022 |
| Economics | Median Income in the Past 12 Months (inflation-adjusted) by race | By race: native hawaiian and other pacific islander | dollars | S1903_C03_006E 
| Economics | Median Income in the Past 12 Months (inflation-adjusted) by race | By race: some other race | dollars | S1903_C03_007E 
| Economics | Mean Income in the Past 12 Months (inflation-adjusted) by race | Mean Income in the Past 12 Months (inflation-adjusted) | dollars | S1902_C03_019E
| Economics | Mean Income in the Past 12 Months (inflation-adjusted) by race | By race: white | dollars | S1902_C03_020E
| Economics | Mean Income in the Past 12 Months (inflation-adjusted) by race | By race: black or african american | dollars | S1902_C03_021E
| Economics | Mean Income in the Past 12 Months (inflation-adjusted) by race | By race: american indian and alaska native | dollars | S1902_C03_022E
| Economics | Mean Income in the Past 12 Months (inflation-adjusted) by race | By race: asian | dollars | S1902_C03_023E 
| Economics | Mean Income in the Past 12 Months (inflation-adjusted) by race | By race: native hawaiian and other pacific islander | dollars | S1902_C03_024E
| Economics | Mean Income in the Past 12 Months (inflation-adjusted) by race | By race: some other race | dollars | S1902_C03_025E 
| Housing | Aggregate Contract Rent | Aggregate Contract Rent | dollars | B25060_001E 
| Housing | Aggregate Contract Rent | Median Contract Rent | dollars | B25058_001E 
| Housing | Aggregate Contract Rent | Lower Contract Rent Quartile | dollars | B25057_001E 
| Housing | Aggregate Contract Rent | Upper Contract Rent Quartile | dollars | B25059_001E 
| Housing | Total Number of Households | Total Number of Households | # of people | B11001_001E 
| Housing | Total Number of Households | Total Number of Family Household | # of people | B11001_002EA 
| Housing | Total Number of Households | Total Number of Non-family Household | # of people | B11001_007E 
| Education | Median Earnings in the Past 12 Months | Median Earnings in the Past 12 Months | dollars | S1501_C01_059E 
| Education | Median Earnings in the Past 12 Months | Less Than High School Graduate | dollars | S1501_C01_060E 
| Education | Median Earnings in the Past 12 Months | High School Graduate | dollars | S1501_C01_061E 
| Education | Median Earnings in the Past 12 Months | Some College and Associate's Degree | dollars | S1501_C01_062E 
| Education | Median Earnings in the Past 12 Months | Bachelor's Degree | dollars | S1501_C01_063E 
| Education | Median Earnings in the Past 12 Months | Graduate or Professional Degree | dollars | S1501_C01_064E 
| Education | Population 3 years and over enrolled in school | Population 3 years and over enrolled in school | # of people | S1401_C01_001E 
| Education | Population 3 years and over enrolled in school | Nursery School, preschool | # of people | S1401_C01_002E 
| Education | Population 3 years and over enrolled in school | Kindergarten to 12th Grade | # of people | S1401_C01_003E 
| Education | Population 3 years and over enrolled in school | College, Undergraduate | # of people | S1401_C01_008E 
| Education | Population 3 years and over enrolled in school | Graduate or Professional School | # of people | S1401_C01_009E 
| Health | Total Population With Disability | Total Population With Disability | # of people | S1810_C02_001E 
| Health | Total Population With Disability | With a hearing difficulty | # of people | S1810_C02_019E 
| Health | Total Population With Disability | With a vision difficulty | # of people | S1810_C02_029E 
| Health | Total Population With Disability | With a cognitive difficulty | # of people | S1810_C02_039E 
| Health | Total Population With Disability | With an ambulatory difficulty | # of people | S1810_C02_047E 
| Health | Total Population With Disability | With a self-care difficulty | # of people | S1810_C02_055E 
| Health | Total Population With Disability | With an independent living difficulty | # of people | S1810_C02_063E 
| Health | Insurance Coverage: Total Population | Insurance Coverage: Total Population | # of people | S2701_C01_001E 
| Health | Insurance Coverage: Total Population | Insured | # of people | S2701_C02_001E
| Health | Insurance Coverage: Total Population | Uninsured | # of people | S2701_C04_001E 
| Population | Total Population and Race Group | Total Population and Race Group | # of people | DP05_0033E 
| Population | Total Population and Race Group | White alone | # of people | DP05_0037E 
| Population | Total Population and Race Group | Black or African American alone | # of people | DP05_0038E 
| Population | Total Population and Race Group | American Indian and Alaska Native alone | # of people | DP05_0039E 
| Population | Total Population and Race Group | Asian | # of people | DP05_0044E | 5-year estimate: 2017-2022 |
| Population | Total Population and Race Group | Native Hawaiian and Other Pacific Islander alone | # of people | DP05_0052E 
| Population | Total Population and Race Group | Some Other Race alone | # of people | DP05_0057E 
| Population | Total Population and Race Group | Two or more races | # of people | DP05_0058E 
| Population | Median Age | Median Age | # of people | B01002_001E 
| Population | Median Age | Female | # of people | B01002_003E 
| Population | Median Age | Male | # of people | B01002_002E 


- Database Models and ERD, please see models.md
https://github.com/uchicago-capp-30320/DataForGood-chicago/blob/main/docs/models.md

- Data Flow: When a user interacts with the application and selects specific parameters (geographic level, indicator category, and years), the backend retrieves the relevant data from the database models and sends it to the frontend for data tables and visualizations. We would like to note that our application allows the user to select indicators within one broader category - i.e. only selecting economic indicator variables - so that users can get a deeper view of one category at a time.

- Dependency Graph
<>
The graph shows the relationships between the different entities in the ERD:

<>


### Frontend and User Interface:
<final design images here>

### Key Concepts:

1. Data Table and Data Visualization: After the user selects the desired parameters, the frontend receives the data from the backend and generates data tables and visualizations. Users can select a specifc year for sub-indicators and heatmap to view the condition on yearly basis. The following is a list of filters that are available for users to customize:
    - Geographic Levels: Users can explore data at different geographic granularities, such as citywide, by zip codes, by community areas, and by census tracts.
    - Indicator Categories: The application provides data across various categories, including population, education, economics, housing, and health characteristics.
    - Years: Users can select a set of 5-year estimates (e.g., 2017-2021 and 2018-2022 ACS 5-year estimates) to view the data for these time periods.

2. Memo generation: The application allows users to press a button to generate memo based on the selected view of data tables and data visualizations
3. Data Export: The application allows users to export the data tables and visualizations in various formats, including Excel (.xlsx), .csv, and .JPEG.
4. Resource: The application allows users to interact with the embedded ArcGIS Instant App to view city resources.
5. Endpoints:
    - /main/aboutus: Displays information about the project, including a description and objectives.
    - /main/data&visualize: The main page for data visualization, where users can select parameters and view data tables and charts.
    - /main/resources: Provides an embedded ArcGIS web app with interactive feature layers.
