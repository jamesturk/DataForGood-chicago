# DataForGood Chicago

### **Project Description**
The main objective of our web application is to help small and medium-sized nonprofits collect, analyze, and use Census data efficiently to achieve their goals. By using advanced technologies like Python, GIS mapping, and data science techniques, including natural language processing and AI, the application will allow nonprofits to easily access and use the city's resources and information, plan strategically, and make data-driven decisions without needing extensive technical skills.

Key components include:
- Data and Dashboard: Select variables and indicators for analysis, generate interactive visualizations, and customizable dashboards for comprehensive insights.
- Automated Insights and Memo Generation: Summarize key insights from data and visuals, generate ready-to-use memos or paragraphs.
- Maps and City Resources: Explore and navigate city resources using integrated ArcGIS Online functionality.

Overall, the application aims to bridge the gap between data availability, accessibility, and its effective utilization by nonprofit organizations. It seeks to empower nonprofits to make informed decisions, optimize resource navigation and allocation, and enhance their impact on the communities they serve.

### **Team Member and Team Roles**
- Bryan Foo Suon Chuang: Lead Frontend Engineer, Supporting QA Engineer, Supporting GIS Engineer
- Yujie Jiang: Lead Backend Engineer/Data Engineer, Supporting UI/UX Designer
- Ruoyi Wu: Lead QA Engineer, Supporting Backend Engineer/Data Engineer
- Yueyue Wang: Lead GIS Engineer, Chief Architect, Supporting Frontend Engineer
- Maxine Xu: Project Manager, Lead UI/UX Designer, Supporting Backend Engineer/Data Engineer

### **Repository Layout**
![image](https://github.com/uchicago-capp-30320/DataForGood-chicago/assets/111541644/188e7962-27e7-4355-97fd-5578f09373fb)
__________________
#### Issue Tracker: Using GitHub Issue Tracker

#### Code Review Process

Steps:
1. Our project employs a code review process beginning with developers submitting a pull request (PR) to the relevant branch.
2. PRs are then automatically assigned to an appropriate reviewer, typically a support role in the relevant domain. The review focuses on code quality, project standards, and functionality, with developers making necessary revisions based on feedback.
3. After reviewer approval, a QA Engineer conducts a final check, ensuring the PR meets all quality benchmarks before the final merge is approved by a Project Manager or Chief Architect.

__________________

#### **Packages used**
Check our pyproject.toml file for all the packages used. Some include:
- census
- django
- pandas


#### **Data Source**

(1) Census API:\
Source: U.S. Census Bureau\
Way of Collection: API Key

(2) ChatGPT API:\

##### Getting Census API key
- Request an API key with this link: https://api.census.gov/data/key_signup.html
- Once you have a key, create a new file called `.env` in the root directory of this project by running `touch .env`.
- In this .env file, assign the key to the variable `CENSUS_API_KEY` without spaces or quotations (i.e. CENSUS_API_KEY=123456789)

- An example of requesting census data and shapefile to map the results are in [this notebook](census_test.ipynb)
__________________

#### **Launching our web application**

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
