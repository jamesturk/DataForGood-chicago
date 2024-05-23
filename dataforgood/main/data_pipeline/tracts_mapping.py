import pandas as pd
# census tract data pulled from:
#https://data.cityofchicago.org/dataset/CensusTractsTIGER2010/74p9-q2aq/about_data
tracts = pd.read_csv('CensusTractsTIGER2010.csv')
tracts = tracts.drop(['the_geom', 'STATEFP10', 'COUNTYFP10', 'COMMAREA_N', 
                      'NOTES'], axis=1)

# community area data pulled from:
# https://www.chicago.gov/content/dam/city/depts/doit/general/GIS/Chicago_Maps/Citywide_Maps/Community_Areas_W_Numbers.pdf

communities = {
    'AREA_NUMBER': [
        35, 36, 37, 38, 39, 4, 40, 41, 42, 1, 11, 12, 13, 14, 15, 16, 17, 18, 
        19, 2, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 3, 30, 31, 33, 34, 10, 
        8, 32, 43, 44, 45, 46, 47, 59, 6, 48, 49, 5, 50, 51, 52, 53, 54, 55, 
        56, 57, 58, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 7, 70, 71, 72, 
        73, 74, 75, 76, 77, 9
    ],
    'COMMUNITY': [
        'DOUGLAS', 'OAKLAND', 'FULLER PARK', 'GRAND BOULEVARD', 'KENWOOD', 
        'LINCOLN SQUARE','WASHINGTON PARK', 'HYDE PARK', 'WOODLAWN', 
        'ROGERS PARK', 'JEFFERSON PARK', 'FOREST GLEN', 'NORTH PARK', 
        'ALBANY PARK', 'PORTAGE PARK', 'IRVING PARK', 'DUNNING', 'MONTCLARE', 
        'BELMONT CRAGIN', 'WEST RIDGE', 'HERMOSA', 'AVONDALE', 'LOGAN SQUARE', 
        'HUMBOLDT PARK', 'WEST TOWN', 'AUSTIN', 'WEST GARFIELD PARK',
        'EAST GARFIELD PARK', 'NEAR WEST SIDE', 'NORTH LAWNDALE', 'UPTOWN', 
        'SOUTH LAWNDALE', 'LOWER WEST SIDE', 'NEAR SOUTH SIDE', 
        'ARMOUR SQUARE', 'NORWOOD PARK', 'NEAR NORTH SIDE',
        'LOOP', 'SOUTH SHORE', 'CHATHAM', 'AVALON PARK', 'SOUTH CHICAGO', 
        'BURNSIDE', 'MCKINLEY PARK', 'LAKE VIEW', 'CALUMET HEIGHTS', 
        'ROSELAND', 'NORTH CENTER','PULLMAN', 'SOUTH DEERING', 'EAST SIDE', 
        'WEST PULLMAN', 'RIVERDALE', 'HEGEWISCH', 'GARFIELD RIDGE', 
        'ARCHER HEIGHTS', 'BRIGHTON PARK', 'BRIDGEPORT', 'NEW CITY',
        'WEST ELSDON', 'GAGE PARK', 'CLEARING', 'WEST LAWN', 'CHICAGO LAWN', 
        'WEST ENGLEWOOD', 'ENGLEWOOD', 'GREATER GRAND CROSSING', 
        'LINCOLN PARK', 'ASHBURN', 'AUBURN GRESHAM', 'BEVERLY', 
        'WASHINGTON HEIGHTS', 'MOUNT GREENWOOD', 'MORGAN PARK', 'OHARE', 
        'EDGEWATER','EDISON PARK'
    ]
}

comms = pd.DataFrame(communities)
comms.columns = ['COMMAREA', 'COMMNAME']
comms['COMMAREA'] = comms['COMMAREA'].astype(int)

# merging tracts and community areas
tracts_comm = pd.merge(tracts, comms, on="COMMAREA", how="left")

# loading in tract and zip code data 
zipcode = pd.read_csv('TRACT_ZIP_122023.csv')
zipcode = zipcode.drop(['RES_RATIO', 'BUS_RATIO', 'OTH_RATIO', 'TOT_RATIO'], axis=1)
zipcode = zipcode.rename(columns={"TRACT": "GEOID10"})

# merging tracts + community data with zip code data
mapping_data = pd.merge(tracts_comm, zipcode, on="GEOID10", how='left')
mapping_data = mapping_data.drop(['USPS_ZIP_PREF_CITY', 'USPS_ZIP_PREF_STATE',
                                'NAMELSAD10'], axis=1)
mapping_data["ZIP"] = mapping_data["ZIP"].astype(str).str.rstrip('.0')

# renaming columns according to models
mapping_data = mapping_data.rename(columns={"TRACTCE10": "census_tract_id", 
                                            "GEOID10": "census_tract_id_11", 
                                            "NAME10": "census_tract_name", 
                                            "COMMAREA": "community_id", 
                                            "COMMNAME": "community_name", 
                                            "ZIP":"zip_code"})

mapping_data.to_csv('census_tracts.csv')
