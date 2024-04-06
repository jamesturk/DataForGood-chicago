## Data For Good

### Getting Census API key
- Request an API key with this link: https://api.census.gov/data/key_signup.html
- Once you have a key, create a new file called `.env` in the root directory of this project by running `touch .env`.
- In this .env file, assign the key to the variable `CENSUS_API_KEY` without spaces or quotations (i.e. CENSUS_API_KEY=123456789)

- An example of requesting census data and shapefile to map the results are in [this notebook](census_test.ipynb)