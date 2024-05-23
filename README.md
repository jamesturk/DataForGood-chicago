# DataForGood Chicago

### **Project Description**
The main objective of our web application is to help small and medium-sized nonprofits collect, analyze, and use Census data efficiently to achieve their goals. By using advanced technologies like Python, GIS mapping, and data science techniques, including natural language processing and AI, the application will allow nonprofits to easily access and use the city's resources and information, plan strategically, and make data-driven decisions without needing extensive technical skills.

Key components include:
- Data and Dashboard: Select variables and indicators for analysis, generate interactive visualizations, and customizable dashboards for comprehensive insights.
- Automated Memo Generation: Summarize key insights from data and visuals, generate ready-to-use memos or paragraphs.
- Maps and City Resources: Explore and navigate city resources using integrated ArcGIS Online functionality.

Overall, the application aims to bridge the gap between data availability, accessibility, and its effective utilization by nonprofit organizations. It seeks to empower nonprofits to make informed decisions, optimize resource navigation and allocation, and enhance their impact on the communities they serve.

### **Team Member and Team Roles**
- Bryan Foo Suon Chuang: Lead Frontend Engineer, Supporting QA Engineer
- Yujie Jiang: Supporting Backend Engineer/Data Engineer, Lead UI/UX Designer
- Ruoyi Wu: Lead QA Engineer, Lead Backend Engineer
- Yueyue Wang: Chief Architect, Supporting Frontend Engineer, Supporting GIS Engineer,
- Maxine Xu: Project Manager, Lead GIS Engineer, Supporting Backend Engineer/Data Engineer

#### **Code Contribution:**
For a detailed description of each team member's code contribution, please see our "Code Ownership.pdf" file in the docs repository.

### **Repository Layout**
```
DataForGood-chicago
├── LICENSE
├── README.md
├── dataforgood: contains code for the web app, including settings, URLs, views, models, templates, and static files.
│   ├── admin_login_info.text
│   ├── dataforgood
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-311.pyc
│   │   │   ├── settings.cpython-311.pyc
│   │   │   ├── urls.cpython-311.pyc
│   │   │   └── wsgi.cpython-311.pyc
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── main: Django app for the main functionality of the web app
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-311.pyc
│   │   │   ├── admin.cpython-311.pyc
│   │   │   ├── apps.cpython-311.pyc
│   │   │   ├── forms.cpython-311.pyc
│   │   │   ├── models.cpython-311.pyc
│   │   │   ├── urls.cpython-311.pyc
│   │   │   ├── utils.cpython-311.pyc
│   │   │   └── views.cpython-311.pyc
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── censustracts: shape files for Chicago's census tracts from City of Chicago's Data Portal
│   │   ├── communityarea: shape files for Chicago's community areas from City of Chicago's Data Portal
│   │   ├── forms.py
│   │   ├── management:
│   │   │   └── commands
│   │   │       ├── __init__.py
│   │   │       └── load_data.py
│   │   ├── models.py
│   │   ├── static: Directory for static files (e.g., CSS, images, JavaScript).
│   │   │   ├── css
│   │   │   │   └── style.css
│   │   │   ├── images
│   │   │   │   ├── banner.webp
│   │   │   │   └── bg.jpg
│   │   │   └── js
│   │   │       └── script.js
│   │   ├── templates: Directory for HTML templates used by Django.
│   │   │   ├── aboutus.html
│   │   │   ├── dataandvisualize.html
│   │   │   ├── index.html
│   │   │   ├── maps
│   │   │   ├── memos
│   │   │   ├── resources.html
│   │   │   └── style.css
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── utils.py
│   │   ├── views.py
│   │   └── zipcode
│   └── manage.py
├── docs: Documentation for our project.
│   ├── architecture.md
│   ├── changelog.md
│   ├── decisions
│   │   └── README.md
│   ├── endpoints
│   │   └── endpoints.md
│   ├── index.md
│   ├── models.md
│   └── test
├── homebrew
├── poetry.lock
└── pyproject.toml
```
__________________
#### Issue Tracker: Using GitHub Issue Tracker

#### Code Review Process

Steps:
1. Our project employs a code review process beginning with developers submitting a pull request (PR) to the relevant branch.
2. PRs are then automatically assigned to an appropriate reviewer, typically a support role in the relevant domain. The review focuses on code quality, project standards, and functionality, with developers making necessary revisions based on feedback.
3. After reviewer approval, a QA Engineer conducts a final check, ensuring the PR meets all quality benchmarks before the final merge is approved by a Project Manager or Chief Architect.

__________________

#### **Packages used**
Check our pyproject.toml file for all the packages used and their relative version. Some include:
- census
- django
- pandas
- python
- pre-commit
- pytest
- requests
- census
- pandas
- psycopg2-binary
- django-extensions
- django-environ
- geopandas
- matplotlib
- numpy
- folium
- python-dotenv
- langchain-openai
- python-docx
- langchain
- docx

#### **Data Source**

(1) Census API:\
Source: U.S. Census Bureau\
Way of Collection: API Key

(2) OpenAI (ChatGPT) API:\
Source: OpenAI\
Way of Collection: API Key

(3) City of Chicago:\
Source: City of Chicago's Data Portal\
Way of Collection: Downloaded shapefiles

#### **Credentials**
##### Getting Census API key
- Census API documentation: https://www.census.gov/data/developers/guidance/api-user-guide.html
- Request an API key with this link: https://api.census.gov/data/key_signup.html
- Once you have the keys, please create a new file called `.env` in the root directory of this project by running `touch .env`.
- In this .env file, assign the key to the variable `CENSUS_API_KEY` without spaces or quotations (i.e. CENSUS_API_KEY=123456789)

- An example of requesting census data and shapefile to map the results are in [this notebook](census_test.ipynb)

##### Getting OpenAI API key
- OpenAI API documentation: https://openai.com/blog/openai-api/
- Create an OpenAI account or sign into your existing account here: https://platform.openai.com/signup
- Once you have a key, assign the key to the variable `open_ai_key` without spaces or quotations (i.e. open_ai_key=123456789)

#### **.env Setup**
- The path of `.env` should look like: DataForGood-chicago/dataforgood/.env

- The format in `.env` should look like the following:
`SECRET_KEY=`\
`DB_NAME=`\
`DB_USER=`\
`DB_PASSWORD=`\
`DB_HOST=`\
`DB_PORT=`\
`open_ai_key=`\
`CENSUS_API_KEY=`

#### **Launching the Web Application**

1. Clone the repository.
```
git clone git@github.com:uchicago-capp-30320/DataForGood-chicago.git
```
2. Navigate to the repository.
```
cd ./DataForGood-chicago/dataforgood
```
3. Ensure that your environment is set up correctly (refer to the above **.env Setup section**)
4. If you haven't done it already:
```
pip install poetry
```
5. Set the path of downloaded poetry
```
export PATH="$HOME/.local/bin:$PATH"
```
6. Establish Dependencies.
```
poetry install
```
7. Activate the virtual environment.
```
poetry shell
```
8. Launch the App
```
python manage.py runserver
```

### **Web App Demo**

#### About Us Page
Our web app has three main tabs: About Us, Data & Visualize, and Resource.\
To navigate to explore and visualize the data, choose "Explore Data" or click on the "Data & Visualize" Tab.

https://github.com/uchicago-capp-30320/DataForGood-chicago/assets/111541644/2bdcad30-70ac-4c71-9c39-1bbcdd75bef6

#### Selecting Geographic Level, Indicator, Years, and Memo Generation

You will be navigated to a new page with a form.

Please choose the geographic level you would like to study. We offer data at the city, community, zip code, and census tract level. In addition to selecting geographic areas, you can also use the search bar to select specific areas you are interested in.

For ease of use, we have grouped the data into five categories: Economic, Education, Health, Housing, and Population. Please select one category and our available data will be generated. In the next field, choose an indicator you would like to analyze in-depth.

https://github.com/uchicago-capp-30320/DataForGood-chicago/assets/111541644/5ee48e72-6118-4254-963b-6d36e2943f30

After choosing an indicator, select the years of data you would like.\
*Please note that are current data consists of the ACS' 5-year estimates, meaning that users should choose non-overlapping years (for example. 2013-2017 and 2018-2022) for the most accurate results.*

If you would like to generate a memo about the key insights of the data, select "Yes" in the "Generate Memo" field.\
*Please note that if you select "Yes" it will take several seconds for the next page to load after clicking the "Submit" button.*

https://github.com/uchicago-capp-30320/DataForGood-chicago/assets/111541644/a33990ea-e6b5-41ce-9cfc-2fbec722497b

#### Tables and Visualizations

After the page loads, scroll down to see the main data table. The table consists of the indicator values for the selected geographic areas and years.

To download the data, select "Download as Excel" or "Download as CSV".

https://github.com/uchicago-capp-30320/DataForGood-chicago/assets/111541644/bde0471b-c99f-419a-bdc5-cc643fa86897

The downloaded data will look like this:

![image](https://github.com/uchicago-capp-30320/DataForGood-chicago/assets/111541644/2702373e-7d53-4348-8892-9e377a31a692)

The first visualization presented to you will be a bar graph of the indicator values for the selected geographic areas and years.

To switch the axes of the bar graph, select the  "Switch Axes" button. To display the bar graph in full screen mode, click on the bar icon to the right and selecting "View in Full screen". Hover over the bars for the geographic area name and the indicator value. 

You are also able to download the bar graph visualization as an PNG, JPEG, PDF or SVG vector image.

https://github.com/uchicago-capp-30320/DataForGood-chicago/assets/111541644/ee03327d-f41d-4a48-8be7-085749d3aea9

The second visualization presented to you will be heat maps of the selected geographic areas and years.

Hover over each geographic area to see the indicator value and the name of the area. Use the "+" button to zoom in, the "-" button to zoom out, and click and drag your mouse to move the frame of the map.

https://github.com/uchicago-capp-30320/DataForGood-chicago/assets/111541644/fb74bbf8-2e52-487a-a8b5-7a27b9fa9a17

#### Subgroup Tables and Visualizations

You are also able to explore the indicator at a deeper level through our subgroups features. 

Choose a specific year of subgroup data and click "Get Data and Visualization" to generate the data tables and visualizations. 

You are able to download the subgroup tables by choosing the "Download as Excel" or "Download as "CSV" buttons as well as switch axes on the bar graph visualization by click the "Switch Axes" button. Hover over the bars for the geographic area name and the indicator value.


https://github.com/uchicago-capp-30320/DataForGood-chicago/assets/111541644/49d581f8-d8b7-4c4b-85cd-f5c67b01d7ee

The downloaded subgroup data will look like this:
![image](https://github.com/uchicago-capp-30320/DataForGood-chicago/assets/111541644/635525ce-39d8-4e94-aab4-bed14660d23e)

#### AI Generated Memo

The generated memo is powered by OpenAI's ChatGPT 3.5 Turbo model. If you selected "Yes" in the data form, the generated memo will be at the bottom of the page.

To download an editable file of the memo, click the "Download Memo" button.

https://github.com/uchicago-capp-30320/DataForGood-chicago/assets/111541644/7619720c-6b35-41ea-b4e1-b9d3c197bfce

The downloaded memo will look like this:
![image](https://github.com/uchicago-capp-30320/DataForGood-chicago/assets/111541644/b4c4dca3-9548-46af-a747-b592ec87494a)

#### Resource Page
To navigate to our Resource page, select the "Resource" tab.

https://github.com/uchicago-capp-30320/DataForGood-chicago/assets/111541644/f253af4b-ece7-4646-bd67-bc5d8853ddbb

Add map elements by selecting the layer icon to the right of the screen and checking the layers you would like to see in the map.

https://github.com/uchicago-capp-30320/DataForGood-chicago/assets/111541644/c31c862c-883b-4b5b-a225-86a85ed86464
