# Base URL for the ACS data
base_url = "https://api.census.gov/data/{year}/acs/acs5"
subject_url = "https://api.census.gov/data/{year}/acs/acs5/subject"
profile_url = "https://api.census.gov/data/{year}/acs/acs5/profile"

# Variables to fetch

# Economics #

# Median Income
#variables = {'main_median_income': "NAME,S1903_C03_001E", 'sub_median_white': "NAME,S1903_C03_002E",
             #'sub_median_black': "NAME,S1903_C03_003E", 'sub_median_ind_ala': "NAME,S1903_C03_004E",
             #'sub_median_asia': "NAME,S1903_C03_005E", 'sub_median_hawai': "NAME,S1903_C03_006E",
             #'sub_median_other': "NAME,S1903_C03_007E"  }

# Mean Income
#variables = {'main_mean_income': "NAME,S1902_C03_019E", 'sub_mean_white': "NAME,S1902_C03_020E",
             #'sub_mean_black': "NAME,S1902_C03_021E", 'sub_mean_ind_ala': "NAME,S1902_C03_022E",
             #'sub_mean_asia': "NAME,S1902_C03_023E", 'sub_mean_hawai': "NAME,S1902_C03_024E",
             #'sub_mean_other': "NAME,S1902_C03_025E"}

# Housing #

# HouseRent
# variables = {'main_agg_rent': "NAME,B25060_001E", 'sub_median_rent': "NAME,B25058_001E", 
             #'sub_lower_rent': "NAME,B25057_001E", 'sub_upper_rent': "NAME,B25059_001E"}
# HouseholdType
#variables = {'main_household_total': "NAME,B11001_001E", 'sub_household_family': "NAME,B11001_002EA", 
             #'sub_household_nonfamily': "NAME,B11001_007E"}


# Education
# median earning
#variables = {'main_median_earning': "NAME,S1501_C01_059E", 'sub_less_high': "NAME,S1501_C01_060E",
             #'sub_high': "NAME,S1501_C01_061E", 'sub_college': "NAME,S1501_C01_062E",
             #'sub_bachelor': "NAME,S1501_C01_063E", 'sub_grad': "NAME,S1501_C01_064E"}

# enrollment
#variables = {'main_enroll': "NAME,S1401_C01_001E", 'sub_nursery': "NAME,S1401_C01_002E",
             #'sub_kind_12': "NAME,S1401_C01_003E", 'sub_college': "NAME,S1401_C01_008E",
             #'sub_grad': "NAME,S1401_C01_009E"}

# Health #
# Disability
#variables = {'main_disability': "NAME,S1810_C02_001E", 'sub_hearing': "NAME,S1810_C02_019E",
             #'sub_vision': "NAME,S1810_C02_029E", 'sub_cognitive': "NAME,S1810_C02_039E",
             #'sub_ambulatory': "NAME,S1810_C02_047E", 'sub_self_care': "NAME,S1810_C02_055E",
             #'sub_ind_living': "NAME,S1810_C02_063E"}

# Insurance
#variables = {'main_population': "NAME,S2701_C01_001E", 'sub_insured': "NAME,S2701_C02_001E",
             #'sub_uninsured': "NAME,S2701_C04_001E"}

# Population #
# Races

#variables = {'main_population': "NAME,DP05_0033E", 'sub_pop_white': "NAME,DP05_0037E",
             #'sub_pop_black': "NAME,DP05_0038E", 'sub_pop_ind_ala': "NAME,DP05_0039E",
             #'sub_pop_asia': "NAME,DP05_0044E", 'sub_pop_hawai': "NAME,DP05_0052E",
             #'sub_pop_other': "NAME,DP05_0057E", 'sub_pop_two': "NAME,DP05_0058E"}

variables = {'main_median_age': "NAME,B01002_001E", 'sub_male_age': "NAME,B01002_002E",
             'sub_female_age': "NAME,B01002_003E"}

# Location filters
location = "for=tract:*&in=state:17+county:031"