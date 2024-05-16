## Architecture Documentation
Welcome to the DataForGood Chicago project! This document will provide you with an overview of our application's architecture and key concepts to help you get started.

### Data Flow and Backend:
- Data Source: The data for our application comes mainly from the American Community Survey conducted by the Census Bureau. We have a backend database using MySQL, which stores this data in a structured format. The following is a table view of the indicators we have for each category:

| Category | Description | Variable Name | Units | Variable Code | Time Unit |
|----------|-------------|---------------|-------|---------------|-----------|
| Economics | Median Income in the Past 12 Months (inflation-adjusted) by race | Median Income in the Past 12 Months (inflation-adjusted) | dollars | S1903_C03_001E | 5-year estimate: 2017-2022 |
| Economics | Median Income in the Past 12 Months (inflation-adjusted) by race | By race: white | dollars | S1903_C03_002E | 5-year estimate: 2017-2022 |
| Economics | Median Income in the Past 12 Months (inflation-adjusted) by race | By race: black or african american | dollars | S1903_C03_003E | 5-year estimate: 2017-2022 |
| Economics | Median Income in the Past 12 Months (inflation-adjusted) by race | By race: american indian and alaska native | dollars | S1903_C03_004E | 5-year estimate: 2017-2022 |
| Economics | Median Income in the Past 12 Months (inflation-adjusted) by race | By race: asian | dollars | S1903_C03_005E | 5-year estimate: 2017-2022 |
| Economics | Median Income in the Past 12 Months (inflation-adjusted) by race | By race: native hawaiian and other pacific islander | dollars | S1903_C03_006E | 5-year estimate: 2017-2022 |
| Economics | Median Income in the Past 12 Months (inflation-adjusted) by race | By race: some other race | dollars | S1903_C03_007E | 5-year estimate: 2017-2022 |
| Economics | Mean Income in the Past 12 Months (inflation-adjusted) by race | Mean Income in the Past 12 Months (inflation-adjusted) | dollars | S1902_C03_019E | 5-year estimate: 2017-2022 |
| Economics | Mean Income in the Past 12 Months (inflation-adjusted) by race | By race: white | dollars | S1902_C03_020E | 5-year estimate: 2017-2022 |
| Economics | Mean Income in the Past 12 Months (inflation-adjusted) by race | By race: black or african american | dollars | S1902_C03_021E | 5-year estimate: 2017-2022 |
| Economics | Mean Income in the Past 12 Months (inflation-adjusted) by race | By race: american indian and alaska native | dollars | S1902_C03_022E | 5-year estimate: 2017-2022 |
| Economics | Mean Income in the Past 12 Months (inflation-adjusted) by race | By race: asian | dollars | S1902_C03_023E | 5-year estimate: 2017-2022 |
| Economics | Mean Income in the Past 12 Months (inflation-adjusted) by race | By race: native hawaiian and other pacific islander | dollars | S1902_C03_024E | 5-year estimate: 2017-2022 |
| Economics | Mean Income in the Past 12 Months (inflation-adjusted) by race | By race: some other race | dollars | S1902_C03_025E | 5-year estimate: 2017-2022 |
| Housing | Aggregate Contract Rent | Aggregate Contract Rent | dollars | B25060_001E | 5-year estimate: 2017-2022 |
| Housing | Aggregate Contract Rent | Median Contract Rent | dollars | B25058_001E | 5-year estimate: 2017-2022 |
| Housing | Aggregate Contract Rent | Lower Contract Rent Quartile | dollars | B25057_001E | 5-year estimate: 2017-2022 |
| Housing | Aggregate Contract Rent | Upper Contract Rent Quartile | dollars | B25059_001E | 5-year estimate: 2017-2022 |
| Housing | Total Number of Households | Total Number of Households | # of people | B11001_001E | 5-year estimate: 2017-2022 |
| Housing | Total Number of Households | Total Number of Family Household | # of people | B11001_002EA | 5-year estimate: 2017-2022 |
| Housing | Total Number of Households | Total Number of Non-family Household | # of people | B11001_007E | 5-year estimate: 2017-2022 |
| Education | Median Earnings in the Past 12 Months | Median Earnings in the Past 12 Months | dollars | S1501_C01_059E | 5-year estimate: 2017-2022 |
| Education | Median Earnings in the Past 12 Months | Less Than High School Graduate | dollars | S1501_C01_060E | 5-year estimate: 2017-2022 |
| Education | Median Earnings in the Past 12 Months | High School Graduate | dollars | S1501_C01_061E | 5-year estimate: 2017-2022 |
| Education | Median Earnings in the Past 12 Months | Some College and Associate's Degree | dollars | S1501_C01_062E | 5-year estimate: 2017-2022 |
| Education | Median Earnings in the Past 12 Months | Bachelor's Degree | dollars | S1501_C01_063E | 5-year estimate: 2017-2022 |
| Education | Median Earnings in the Past 12 Months | Graduate or Professional Degree | dollars | S1501_C01_064E | 5-year estimate: 2017-2022 |
| Education | Population 3 years and over enrolled in school | Population 3 years and over enrolled in school | # of people | S1401_C01_001E | 5-year estimate: 2017-2022 |
| Education | Population 3 years and over enrolled in school | Nursery School, preschool | # of people | S1401_C01_002E | 5-year estimate: 2017-2022 |
| Education | Population 3 years and over enrolled in school | Kindergarten to 12th Grade | # of people | S1401_C01_003E | 5-year estimate: 2017-2022 |
| Education | Population 3 years and over enrolled in school | College, Undergraduate | # of people | S1401_C01_008E | 5-year estimate: 2017-2022 |
| Education | Population 3 years and over enrolled in school | Graduate or Professional School | # of people | S1401_C01_009E | 5-year estimate: 2017-2022 |
| Health | Total Population With Disability | Total Population With Disability | # of people | S1810_C02_001E | 5-year estimate: 2017-2022 |
| Health | Total Population With Disability | With a hearing difficulty | # of people | S1810_C02_019E | 5-year estimate: 2017-2022 |
| Health | Total Population With Disability | With a vision difficulty | # of people | S1810_C02_029E | 5-year estimate: 2017-2022 |
| Health | Total Population With Disability | With a cognitive difficulty | # of people | S1810_C02_039E | 5-year estimate: 2017-2022 |
| Health | Total Population With Disability | With an ambulatory difficulty | # of people | S1810_C02_047E | 5-year estimate: 2017-2022 |
| Health | Total Population With Disability | With a self-care difficulty | # of people | S1810_C02_055E | 5-year estimate: 2017-2022 |
| Health | Total Population With Disability | With an independent living difficulty | # of people | S1810_C02_063E | 5-year estimate: 2017-2022 |
| Health | Insurance Coverage: Total Population | Insurance Coverage: Total Population | # of people | S2701_C01_001E | 5-year estimate: 2017-2022 |
| Health | Insurance Coverage: Total Population | Insured | # of people | S2701_C02_001E | 5-year estimate: 2017-2022 |
| Health | Insurance Coverage: Total Population | Uninsured | # of people | S2701_C04_001E | 5-year estimate: 2017-2022 |
| Population | Total Population and Race Group | Total Population and Race Group | # of people | DP05_0033E | 5-year estimate: 2017-2022 |
| Population | Total Population and Race Group | White alone | # of people | DP05_0037E | 5-year estimate: 2017-2022 |
| Population | Total Population and Race Group | Black or African American alone | # of people | DP05_0038E | 5-year estimate: 2017-2022 |
| Population | Total Population and Race Group | American Indian and Alaska Native alone | # of people | DP05_0039E | 5-year estimate: 2017-2022 |
| Population | Total Population and Race Group | Asian | # of people | DP05_0044E | 5-year estimate: 2017-2022 |
| Population | Total Population and Race Group | Native Hawaiian and Other Pacific Islander alone | # of people | DP05_0052E | 5-year estimate: 2017-2022 |
| Population | Total Population and Race Group | Some Other Race alone | # of people | DP05_0057E | 5-year estimate: 2017-2022 |
| Population | Total Population and Race Group | Two or more races | # of people | DP05_0058E | 5-year estimate: 2017-2022 |
| Population | Median Age | Median Age | # of people | B01002_001E | 5-year estimate: 2017-2022 |
| Population | Median Age | Female | # of people | B01002_003E | 5-year estimate: 2017-2022 |
| Population | Median Age | Male | # of people | B01002_002E | 5-year estimate: 2017-2022 |


- Database Models:
    - `main_tractzipcode`: This model maps each of Chicago's census tracts to their corresponding zip code.

    - `main_censustracts`: This model maps each of Chicago's census tracts to their corresponding community areas.

    - `main_meanincome_main`: This model stores the mean income of households for each census tract and year.

    - `main_meanincome_sub`: This model stores the mean income of households by race for each census tract and year. The racial categories include: White, Black or African American, Indian and Alaska Native, Asian, Native Hawaiian and other Pacific Islander, and Other.

    - (Note: The provided examples focus on one example of an economic indicator, but similar models exist for other indicator categories like housing, education, etc.)

- Simplified Version of the Entity-Relationship Diagram:
![image](https://github.com/uchicago-capp-30320/DataForGood-chicago/assets/111541644/e86d0b43-2b6a-40bb-b246-8ba29f9368be)

**Please see `models.md` file for a more comprehensive diagram**

- Data Flow: When a user interacts with the application and selects specific parameters (geographic level, indicator category, indicator, and years), the backend retrieves the relevant data from the database models and sends it to the frontend for visualization. We would like to note that our application allows the user to select indicators within one broader category (ie only selecting economic indicator variables) so that users can get a deeper view of one category at a time.

### Frontend and User Interface:
- Draft UI Design:
![image](https://github.com/uchicago-capp-30320/DataForGood-chicago/assets/111541644/e0a4116f-4387-43fb-ba12-9b9a8a17f423)
![image](https://github.com/uchicago-capp-30320/DataForGood-chicago/assets/111541644/39ba059f-3412-41f9-be42-a036aad657b0)
![image](https://github.com/uchicago-capp-30320/DataForGood-chicago/assets/111541644/f0837a66-4884-4da7-b3c7-40731f11d1ce)
![image](https://github.com/uchicago-capp-30320/DataForGood-chicago/assets/111541644/59b9dff0-944b-4941-9927-28c1309365c2)

### Key Concepts:

1. Data Table and Data Visualization: After the user selects the desired parameters, the frontend receives the data from the backend and generates data tables and visualizations. The following is a list of filters that are available for users to customize:
    - Geographic Levels: Users can explore data at different geographic granularities, such as citywide, by zip code, by community area, and by census tracts.
    - Indicator Categories: The application provides data across various categories, including population characteristics, education, economics, and housing.
    - Years: Users can select a specific 5-year estimate or a range of individual years (e.g., 2018-2022 5-year estimate or 2021-2022 yearly) to view the data for those time periods.
    - Indicators: Each indicator category may have indicators that provide more detailed information of the general groups (e.g., *Total Population* within the `population_characteristics`).
    - Sub-indicators: Each indicator category may have indicators that provide more detailed information of the general groups (e.g., breakdown of race groups for the indicator *Total Population*). We will present the data tables and visuals for all sub-indicators, and users can decide to display certain visuals using the dropdowns and download them.

2. Memo generation: The application allows users to select whether they would like to generate memo when they are choosing their desired parameters. Users are also able to download their memo to an editable Word document.

3. Data Export: The application allows users to export the data tables and visualizations in various formats, including Excel (.xlsx), CSV, JPEG, PNG, etc.
   
5. Resource: The application allows users to interact with the embedded ArcGIS Instant App to view city resources.
6. Endpoints:
    - /main/aboutus: Displays information about the project, including a description and objectives.
    - /main/data&visualize: The main page for data visualization, where users can select parameters and view data tables and charts.
    - /main/resources: Provides an embedded ArcGIS web app with interactive feature layers.
    - /main/data&visualize/{parameters from query}/tables.xlsx: Enables the user to download the datatables as one .xlsx file, with each datatable as an excel worksheet tab.
    - /main/data&visualize/{parameters from query}/tables.pdf: Enables the user to download the datatables as a .pdf file, with each datatable as a page in the PDF document.
    - /main/data&visualize/{parameters from query}/chart_1.jpg: There will be one unique link for each chart in the HTML page. This enables the user to select the specific charts to download as a .jpg image, with each image being one chart.
    - /main/resources: Provides a view of an embedded ArcGIS web app.
