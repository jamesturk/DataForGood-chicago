from django.test import TestCase

from .models import CensusTracts, TractZipCode, ContractRent_Main, Races_Main
from .utils import MainTable, SubgroupTable


INDICATORS_LIST = ["Aggregate Contract Rent", "Total Population and Race Group"]

TRACT_LIST = [80400, 80401, 80402, 80403, 80404, 80405]
ZIPCODE_LIST = [60601, 60602, 60603]
COMMUNTIY_LIST = ["HYDE PARK", "LINCOLN PARK", "KENWOOD"]

PERIOD_LIST = [
    "2013-2017",
    "2014-2018",
]


class CreateMainTableTests(TestCase):
    """
    Tests the MainTable class in utils.py that is required to create the
    main data table in the web app.
    """
    def setUp(self):

        # 6 Census Tracts, 3 Zipcodes, 3 Neighborhoods
        CensusTracts.objects.create(tract_id=80400, community="HYDE PARK")
        CensusTracts.objects.create(name=80401, community="HYDE PARK")
        CensusTracts.objects.create(name=80402, community="LINCOLN PARK")
        CensusTracts.objects.create(name=80403, community="LINCOLN PARK")
        CensusTracts.objects.create(name=80404, community="KENWOOD")
        CensusTracts.objects.create(name=80405, community="KENWOOD")

        TractZipCode.objects.create(id=1, tract=80400, zip_code=60601)
        TractZipCode.objects.create(id=2, tract=80401, zip_code=60602)
        TractZipCode.objects.create(id=3, tract=80402, zip_code=60603)
        TractZipCode.objects.create(id=4, tract=80403, zip_code=60601)
        TractZipCode.objects.create(id=5, tract=80404, zip_code=60602)
        TractZipCode.objects.create(id=6, tract=80405, zip_code=60603)

        # Indicator 1 - "Aggregate Contract Rent" (No Missing Data)
        # Aggregation takes the average values across tracts
        indicator_name = "Aggregate Contract Rent"
    
        ContractRent_Main.objects.create(
            id=1,
            sub_group_indicator_name=indicator_name,
            census_tract=80400,
            year=2017,
            value=1000
        )
        ContractRent_Main.objects.create(
            id=2,
            sub_group_indicator_name=indicator_name,
            census_tract=80400,
            year=2018,
            value=1500
        )
        ContractRent_Main.objects.create(
            id=3,
            sub_group_indicator_name=indicator_name,
            census_tract=80401,
            year=2017,
            value=2000
        )
        ContractRent_Main.objects.create(
            id=4,
            sub_group_indicator_name=indicator_name,
            census_tract=80401,
            year=2018,
            value=2200
        )
        ContractRent_Main.objects.create(
            id=5,
            sub_group_indicator_name=indicator_name,
            census_tract=80402,
            year=2017,
            value=3000
        )
        ContractRent_Main.objects.create(
            id=6,
            sub_group_indicator_name=indicator_name,
            census_tract=80402,
            year=2018,
            value=5000
        )
        ContractRent_Main.objects.create(
            id=7,
            sub_group_indicator_name=indicator_name,
            census_tract=80403,
            year=2017,
            value=3000
        )
        ContractRent_Main.objects.create(
            id=8,
            sub_group_indicator_name=indicator_name,
            census_tract=80403,
            year=2018,
            value=2800
        )
        ContractRent_Main.objects.create(
            id=9,
            sub_group_indicator_name=indicator_name,
            census_tract=80404,
            year=2017,
            value=1500
        )
        ContractRent_Main.objects.create(
            id=10,
            sub_group_indicator_name=indicator_name,
            census_tract=80404,
            year=2018,
            value=1700
        )
        ContractRent_Main.objects.create(
            id=11,
            sub_group_indicator_name=indicator_name,
            census_tract=80405,
            year=2017,
            value=800
        )
        ContractRent_Main.objects.create(
            id=12,
            sub_group_indicator_name=indicator_name,
            census_tract=80405,
            year=2018,
            value=1000
        )


        # Indicator 2 - "Total Population and Race Group" (With Missing Data)
        # Aggregation takes the sum of values across tracts
        # Tract 80405 not included in database
        # 2015-2018 data for Tract 80404 not available
        indicator_name = "Total Population and Race Group"

        Races_Main.objects.create(
            id=1,
            sub_group_indicator_name=indicator_name,
            census_tract=80400,
            year=2017,
            value=10000
        )
        Races_Main.objects.create(
            id=2,
            sub_group_indicator_name=indicator_name,
            census_tract=80400,
            year=2018,
            value=15000
        )
        Races_Main.objects.create(
            id=3,
            sub_group_indicator_name=indicator_name,
            census_tract=80401,
            year=2017,
            value=20000
        )
        Races_Main.objects.create(
            id=4,
            sub_group_indicator_name=indicator_name,
            census_tract=80401,
            year=2018,
            value=22000
        )
        Races_Main.objects.create(
            id=5,
            sub_group_indicator_name=indicator_name,
            census_tract=80402,
            year=2017,
            value=30000
        )
        Races_Main.objects.create(
            id=6,
            sub_group_indicator_name=indicator_name,
            census_tract=80402,
            year=2018,
            value=50000
        )
        Races_Main.objects.create(
            id=7,
            sub_group_indicator_name=indicator_name,
            census_tract=80403,
            year=2017,
            value=30000
        )
        Races_Main.objects.create(
            id=8,
            sub_group_indicator_name=indicator_name,
            census_tract=80403,
            year=2018,
            value=28000
        )
        Races_Main.objects.create(
            id=9,
            sub_group_indicator_name=indicator_name,
            census_tract=80404,
            year=2017,
            value=15000
        )
    
    def test_rent_main_city_level(self):
        """
        """
        geographic_level = "City of Chicago"
        geographic_unit = []
        indicator = "Aggregate Contract Rent"
        model = ContractRent_Main
        periods = PERIOD_LIST

        rows = MainTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).table["rows"]
        
        correct_rows = [
            ["City of Chicago", 1883.33, 2366.67]
        ]

        self.assertEqual(rows == correct_rows)
    
    def test_rent_main_community_level(self):
        """
        """
        geographic_level = "Community"
        geographic_unit = COMMUNTIY_LIST
        indicator = "Aggregate Contract Rent"
        model = ContractRent_Main
        periods = PERIOD_LIST

        rows = MainTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).table["rows"]
        
        correct_rows = [
            ["HYDE PARK", 1500, 1850]
            ["LINCOLN PARK", 3000, 3900]
            ["KENWOOD", 1150, 1350]
        ]

        self.assertEqual(rows == correct_rows)
    
    def test_rent_main_zipcode_level(self):
        """
        """
        geographic_level = "Zipcode"
        geographic_unit = ZIPCODE_LIST
        indicator = "Aggregate Contract Rent"
        model = ContractRent_Main
        periods = PERIOD_LIST

        rows = MainTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).table["rows"]
        
        correct_rows = [
            [60601, 2000, 2150]
            [60602, 2150, 1950]
            [60603, 1900, 3000]
        ]

        self.assertEqual(rows == correct_rows)
    
    def test_rent_main_tract_level(self):
        """
        """
        geographic_level = "Tract"
        geographic_unit = TRACT_LIST
        indicator = "Aggregate Contract Rent"
        model = ContractRent_Main
        periods = PERIOD_LIST

        rows = MainTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).table["rows"]
        
        correct_rows = [
            [80400, 1000, 1500]
            [80401, 2000, 2200]
            [80402, 3000, 5000]
            [80403, 3000, 2800]
            [80404, 1500, 1700]
            [80405, 800, 1000]
        ]

        self.assertEqual(rows == correct_rows)

    def test_pop_main_city_level(self):
        """
        """
        geographic_level = "City of Chicago"
        geographic_unit = []
        indicator = "Aggregate Contract Rent"
        model = Races_Main
        periods = PERIOD_LIST

        rows = MainTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).table["rows"]
        
        correct_rows = [
            ["City of Chicago", 105000, 115000]
        ]

        self.assertEqual(rows == correct_rows)
    
    def test_pop_main_community_level(self):
        """
        """
        geographic_level = "Community"
        geographic_unit = COMMUNTIY_LIST
        indicator = "Aggregate Contract Rent"
        model = Races_Main
        periods = PERIOD_LIST

        rows = MainTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).table["rows"]
        
        correct_rows = [
            ["HYDE PARK", 30000, 37000]
            ["LINCOLN PARK", 60000, 78000]
            ["KENWOOD", 15000, "NA"]
        ]

        self.assertEqual(rows == correct_rows)
    
    def test_pop_main_zipcode_level(self):
        """
        """
        geographic_level = "Zipcode"
        geographic_unit = ZIPCODE_LIST
        indicator = "Aggregate Contract Rent"
        model = Races_Main
        periods = PERIOD_LIST

        rows = MainTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).table["rows"]
        
        correct_rows = [
            [60601, 40000, 43000]
            [60602, 35000, 22000]
            [60603, 30000, 50000]
        ]

        self.assertEqual(rows == correct_rows)
    
    def test_pop_main_tract_level(self):
        """
        """
        geographic_level = "Tract"
        geographic_unit = TRACT_LIST
        indicator = "Aggregate Contract Rent"
        model = Races_Main
        periods = PERIOD_LIST

        rows = MainTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).table["rows"]
        
        correct_rows = [
            [80400, 10000, 15000]
            [80401, 20000, 22000]
            [80402, 30000, 50000]
            [80403, 30000, 28000]
            [80404, 15000, "NA"]
            [80405, "NA", "NA"]
        ]

        self.assertEqual(rows == correct_rows)
    