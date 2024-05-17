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
│   ├── db.sqlite3
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
├── dfg_chi
│   ├── __init__.py
│   ├── backend
│   │   ├── data_downloaded
│   │   │   ├── Economics
│   │   │   │   ├── MeanIncome
│   │   │   │   │   ├── main
│   │   │   │   │   └── sub
│   │   │   │   ├── MedianIncome
│   │   │   │   │   ├── main
│   │   │   │   │   └── sub
│   │   │   │   └── README
│   │   │   ├── Education
│   │   │   │   ├── Enrollment
│   │   │   │   │   ├── main
│   │   │   │   │   └── sub
│   │   │   │   └── MedianEarning
│   │   │   │       ├── main
│   │   │   │       └── sub
│   │   │   ├── Health
│   │   │   │   ├── Disability
│   │   │   │   │   ├── main
│   │   │   │   │   └── sub
│   │   │   │   └── Insurance
│   │   │   │       ├── main
│   │   │   │       └── sub
│   │   │   ├── Housing
│   │   │   │   ├── ContractRent
│   │   │   │   │   ├── README
│   │   │   │   │   ├── main
│   │   │   │   │   └── sub
│   │   │   │   ├── HouseholdType
│   │   │   │   │   ├── README
│   │   │   │   │   ├── main
│   │   │   │   │   └── sub
│   │   │   │   └── README
│   │   │   ├── Population
│   │   │   │   ├── MedianAge
│   │   │   │   │   ├── main
│   │   │   │   │   └── sub
│   │   │   │   └── Races
│   │   │   │       ├── main
│   │   │   │       └── sub
│   │   │   ├── census_tracts.csv
│   │   │   └── data_5yr
│   │   └── variables.json
│   ├── gis
│   │   └── README.md
│   ├── main.py
│   ├── static
│   │   ├── README.md
│   │   ├── bootstrap
│   │   │   └── README.md
│   │   ├── css
│   │   │   └── README.md
│   │   └── js
│   │       └── README.md
│   └── templates
│       └── README.md
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

(2) OpenAI API:\
Source: OpenAI\
Way of Collection: API Key

(3) City of Chicago:\
Source: City of Chicago's Data Portal\
Way of Collection: Downloaded shapefiles

#### **Credentials**
##### Getting Census API key
- Request an API key with this link: https://api.census.gov/data/key_signup.html
- Once you have the keys, please create a new file called `.env` in the root directory of this project by running `touch .env`.
- In this .env file, assign the key to the variable `CENSUS_API_KEY` without spaces or quotations (i.e. CENSUS_API_KEY=123456789)

- An example of requesting census data and shapefile to map the results are in [this notebook](census_test.ipynb)

##### Getting OpenAI API key
- Create an OpenAI account or sign into your existing account here: https://openai.com/blog/openai-api/
- Once you have a key, assign the key to the variable `open_ai_key` without spaces or quotations (i.e. open_ai_key=123456789)

#### **.env Setup**
- The path of `.env` should look like: DataForGood-chicago/dataforgood/.env
- The format in `.env` should look like the following:
SECRET_KEY=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
open_ai_key=
CENSUS_API_KEY=
__________________

#### **Launching the Web Application**


1. Clone the repository.
```
git clone git@github.com:uchicago-capp-30320/DataForGood-chicago.git
```
2. Navigate to the repository.
```
cd ./DataForGood-chicago/dataforgood
```
3. If you haven't done it already:
```
pip install poetry
```
4. Set the path of downloaded poetry
```
export PATH="$HOME/.local/bin:$PATH"
```
5. Establish Dependencies.
```
poetry install
```
6. Activate the virtual environment.
```
poetry shell
```
5. Launch the App
```
python manage.py runserver
```
