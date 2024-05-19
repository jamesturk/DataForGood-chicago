## Database Models:
`main_tractzipcode`: This model maps each of Chicago's census tracts to their corresponding zip code.

`main_censustracts`: This model maps each of Chicago's census tracts to their corresponding community areas.

`main_meanincome_main`: This model stores the mean income of households for each census tract and year.

`main_meanincome_sub`: This model stores the mean income of households by race for each census tract and year. The racial categories include: White, Black or African American, Indian and Alaska Native, Asian, Native Hawaiian and other Pacific Islander, and Other.

(Note: The provided examples focus on one example of an economic indicator, but similar models exist for other indicator categories like housing, education, etc.)

`main_tractzipcode`:
| Name           | Type           | Description                                                   |
|----------------|----------------|---------------------------------------------------------------|
| id             | PrimaryKey, int| Unique ID number for each tract-zip code mapping              |
| zip_code       | int            | Zip code                                                      |
| tract_id       | ForeignKey (main_censustracts), int            | Census Tract ID                                               |

`main_censustracts`
| Name           | Type           | Description                                                   |
|----------------|----------------|---------------------------------------------------------------|
| tract_id       | PrimaryKey, int| Census Tract ID                                               |
| community      | str            | Community Area Name                                           |

(For example Mean Income of Households): `main_meanincome_main`
| Name           | Type              | Description                                                      |
|----------------|-------------------|------------------------------------------------------------------|
| id             | PrimaryKey, int   | Unique ID for each tract and year                                |
| indicator_id   | int               | ID for each broader indicator category (Economics, Housing, etc) |
| census_tract_id| ForeignKey (main_censustracts), int | Census Tract ID                                 |
| indicator_name | str               | Name of indicator variable (e.g., mean_income)                   |
| year           | int               | Year (value ranges from 2017-2022)                               |
| value          | int               | Median income in US dollars                                      |

(For example Mean Income of Households by Racial Category): `main_meanincome_sub`
| Name           | Type              | Description                                                      |
|----------------|-------------------|------------------------------------------------------------------|
| id             | PrimaryKey, int   | Unique ID for each tract and year                                |
| indicator_id   | int               | ID for each broader indicator category (Economics, Housing, etc) |
| census_tract_id| ForeignKey(main_censustracts), int | Census Tract ID                                 |
| sub_group_indicator_name | str               | Name of indicator variable (e.g., mean_income)                   |
| year           | int               | Year (value ranges from 2017-2022)                               |
| value          | int               | Median income in US dollars                                      |

### Entity-Relationship Diagram:

Simplified Diagram:
![image](https://github.com/uchicago-capp-30320/DataForGood-chicago/assets/111541644/58ddd87d-fd93-429e-a484-9f523d7a323c)

Actual Diagram:
![image](https://github.com/uchicago-capp-30320/DataForGood-chicago/assets/111541644/ee389a26-00f5-43e8-a3f0-fc0088c49cbc)

**For more information on the data flow and backend processes please read the `architecture.md` file.**
