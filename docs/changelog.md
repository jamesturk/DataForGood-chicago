## Changelog
All notable changes to this project will be documented in this file.

### 4.26.2024 Changes
Because the ACS' 1-year estimate data is sometimes missing for certain geographic levels and indicators, we have decided to only include ACS' 5-year estimate data. Consequently, users will only be able to compare non-overlapping years (for example 2013-2017 data and 2018-2022) if they would like to get an accurate analysis of trends.

### 4.29.2024 Changes
Our team decided to switch from MySQL to PostgreSQL as we found that there are more resources on deployment.

### 5.10.2024 Changes
Our team has decided to change the architecture of our database. Previously, we had one schema, called `georeference`, which mapped each census tract to its respective zip code and community area. However, a census tract could correspond to multiple zip codes. Because of this, we decided to separate the georeference schema into `main_tractzipcode` and `main_censustracts`. 

We also decided to download the shapefiles for the heat maps directly from the Chicago Data Portal and store them in the `main` drectory instead of including this information in `main_tractzipcode` and `main_censustracts`.
