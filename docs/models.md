## Database Models:
`geo_reference`: This model contains geographic information such as census tract ID, community name, zip code, latitude, longitude, and geometry (GIS polygon).
`economic_characteristics`: This model stores economic indicators like median income of households for each census tract and year.
`economic_sub_indicator`: This model holds sub-indicators related to economic characteristics, such as median income by race, for each census tract and year.
(Note: The provided examples focus on economic indicators, but similar models exist for other indicator categories like housing, education, etc.)

`geo_reference`:
| Name           | Type           | Description                                                   |
|----------------|----------------|---------------------------------------------------------------|
| id             | PrimaryKey, int| Census Tract ID                                               |
| community_name | str            | Name of the Community                                         |
| zip_code       | int            | Zip code                                                      |
| INTPTLAT       | float          | Latitude of Census Tract                                      |
| INTPTLON       | float          | Longitude of Census Tract                                     |
| geometry       | str            | GIS polygon: Each pair of numbers represents a point in the polygon, with the first number being the x-coordinate and the second number being the y-coordinate. |

`economic_characteristics` (for example Median Income of Households):
| Name           | Type              | Description                                                      |
|----------------|-------------------|------------------------------------------------------------------|
| id             | int               | Unique ID for each tract and year                                |
| indicator_id   | PrimaryKey, int   | ID for each broader indicator category (Economics, Housing, etc) |
| census_tract_id| ForeignKey(georeference), int | Census Tract ID                                            |
| indicator_name | str               | Name of indicator variable (e.g., mean_income)                   |
| year           | int               | Year (value ranges from 2017-2022)                               |
| value          | int               | Median income in US dollars                                      |

`economic_sub_indicator` (for example Median Income of Households by Race):
| Name                   | Type                               | Description                                                            |
|------------------------|------------------------------------|------------------------------------------------------------------------|
| id                     | PrimaryKey, int                   | Unique ID for each tract and year                                      |
| indicator_id           | ForeignKey(economic_characteristics), int | ID for each broader indicator category (Economics, Housing, etc) |
| census_tract_id        | ForeignKey(economic_characteristics), int | Census Tract ID                                                  |
| sub_group_indicator_name | str                               | Name of subcategory (e.g., median_black, median_white, etc.)            |
| year                   | int                                | Year (value ranges from 2017-2022)                                     |
| value                  | int                                | Median income in US dollars                                            |

### Entity-Relationship Diagram:
![image](https://github.com/uchicago-capp-30320/DataForGood-chicago/assets/111541644/c10b12d7-c39d-4ef9-8451-21e7c4e8bc74)

**For more information on the data flow and backend processes please read the `architecture.md` file.**
