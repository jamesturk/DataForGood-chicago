from django.test import TestCase

from .models import (CensusTracts, 
                     TractZipCode, 
                     ContractRent_Main, 
                     Races_Main, 
                     ContractRent_Sub, 
                     Races_Sub
                     )
from .utils import MainTable, SubgroupTable, generate_heatmaps, WriteMemo
import unittest
from django.template import Template, Context
import pandas as pd
import environ

env = environ.Env()
environ.Env.read_env()
open_ai_key = env("open_ai_key")

INDICATORS_LIST = ["Aggregate Contract Rent", "Total Population and Race Group"]

TRACT_LIST = [80400, 80401, 80402, 80403, 80404, 80405]
ZIPCODE_LIST = [60601, 60602, 60603]
COMMUNTIY_LIST = ["HYDE PARK", "LINCOLN PARK", "KENWOOD"]

PERIOD_LIST = [
    "2013-2017",
    "2014-2018",
]

SINGLE_PERIOD_LIST = [
    "2013-2017",
]


class CreateMainTableTests(TestCase):
    """
    Tests the MainTable class in utils.py that is required to create the
    main data table in the web app.
    """
    def setUp(self):

        # 6 Census Tracts, 3 Zipcodes, 3 Neighborhoods
        CensusTracts.objects.create(tract_id=80400, community="HYDE PARK")
        CensusTracts.objects.create(tract_id=80401, community="HYDE PARK")
        CensusTracts.objects.create(tract_id=80402, community="LINCOLN PARK")
        CensusTracts.objects.create(tract_id=80403, community="LINCOLN PARK")
        CensusTracts.objects.create(tract_id=80404, community="KENWOOD")
        CensusTracts.objects.create(tract_id=80405, community="KENWOOD")

        TractZipCode.objects.create(id=1, tract_id=80400, zip_code=60601)
        TractZipCode.objects.create(id=2, tract_id=80401, zip_code=60602)
        TractZipCode.objects.create(id=3, tract_id=80402, zip_code=60603)
        TractZipCode.objects.create(id=4, tract_id=80403, zip_code=60601)
        TractZipCode.objects.create(id=5, tract_id=80404, zip_code=60602)
        TractZipCode.objects.create(id=6, tract_id=80405, zip_code=60603)

        # Indicator 1 - "Aggregate Contract Rent" (No Missing Data)
        # Aggregation takes the average values across tracts
        indicator_1_name = "Aggregate Contract Rent"
    
        ContractRent_Main.objects.create(
            id=1,
            indicator_id=4,
            indicator_name=indicator_1_name,
            census_tract_id=80400,
            year=2017,
            value=1000
        )
        ContractRent_Main.objects.create(
            id=2,
            indicator_id=4,
            indicator_name=indicator_1_name,
            census_tract_id=80400,
            year=2018,
            value=1500
        )
        ContractRent_Main.objects.create(
            id=3,
            indicator_id=4,
            indicator_name=indicator_1_name,
            census_tract_id=80401,
            year=2017,
            value=2000
        )
        ContractRent_Main.objects.create(
            id=4,
            indicator_id=4,
            indicator_name=indicator_1_name,
            census_tract_id=80401,
            year=2018,
            value=2200
        )
        ContractRent_Main.objects.create(
            id=5,
            indicator_id=4,
            indicator_name=indicator_1_name,
            census_tract_id=80402,
            year=2017,
            value=3000
        )
        ContractRent_Main.objects.create(
            id=6,
            indicator_id=4,
            indicator_name=indicator_1_name,
            census_tract_id=80402,
            year=2018,
            value=5000
        )
        ContractRent_Main.objects.create(
            id=7,
            indicator_id=4,
            indicator_name=indicator_1_name,
            census_tract_id=80403,
            year=2017,
            value=3000
        )
        ContractRent_Main.objects.create(
            id=8,
            indicator_id=4,
            indicator_name=indicator_1_name,
            census_tract_id=80403,
            year=2018,
            value=2800
        )
        ContractRent_Main.objects.create(
            id=9,
            indicator_id=4,
            indicator_name=indicator_1_name,
            census_tract_id=80404,
            year=2017,
            value=1500
        )
        ContractRent_Main.objects.create(
            id=10,
            indicator_id=4,
            indicator_name=indicator_1_name,
            census_tract_id=80404,
            year=2018,
            value=1700
        )
        ContractRent_Main.objects.create(
            id=11,
            indicator_id=4,
            indicator_name=indicator_1_name,
            census_tract_id=80405,
            year=2017,
            value=800
        )
        ContractRent_Main.objects.create(
            id=12,
            indicator_id=4,
            indicator_name=indicator_1_name,
            census_tract_id=80405,
            year=2018,
            value=1000
        )


        # Indicator 2 - "Total Population and Race Group" (With Missing Data)
        # Aggregation takes the sum of values across tracts
        # Tract 80405 not included in database
        # 2015-2018 data for Tract 80404 not available
        indicator_2_name = "Total Population and Race Group"

        Races_Main.objects.create(
            id=1,
            indicator_id=5,
            indicator_name=indicator_2_name,
            census_tract_id=80400,
            year=2017,
            value=10000
        )
        Races_Main.objects.create(
            id=2,
            indicator_id=5,
            indicator_name=indicator_2_name,
            census_tract_id=80400,
            year=2018,
            value=15000
        )
        Races_Main.objects.create(
            id=3,
            indicator_id=5,
            indicator_name=indicator_2_name,
            census_tract_id=80401,
            year=2017,
            value=20000
        )
        Races_Main.objects.create(
            id=4,
            indicator_id=5,
            indicator_name=indicator_2_name,
            census_tract_id=80401,
            year=2018,
            value=22000
        )
        Races_Main.objects.create(
            id=5,
            indicator_id=5,
            indicator_name=indicator_2_name,
            census_tract_id=80402,
            year=2017,
            value=30000
        )
        Races_Main.objects.create(
            id=6,
            indicator_id=5,
            indicator_name=indicator_2_name,
            census_tract_id=80402,
            year=2018,
            value=50000
        )
        Races_Main.objects.create(
            id=7,
            indicator_id=5,
            indicator_name=indicator_2_name,
            census_tract_id=80403,
            year=2017,
            value=30000
        )
        Races_Main.objects.create(
            id=8,
            indicator_id=5,
            indicator_name=indicator_2_name,
            census_tract_id=80403,
            year=2018,
            value=28000
        )
        Races_Main.objects.create(
            id=9,
            indicator_id=5,
            indicator_name=indicator_2_name,
            census_tract_id=80404,
            year=2017,
            value=15000
        )
    
    def test_rent_main_city_level(self):
        """
        Tests rows of main data table for a city-level query, without any
        missing data. Aggregation computes the mean across tracts.
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
            ["City Average", 1883.33, 2366.67],
        ]

        self.assertEqual(rows, correct_rows)
    
    def test_rent_main_community_level(self):
        """
        Tests rows of main data table for a community-level query, without any
        missing data. Aggregation computes the mean across tracts.
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
            ["Hyde Park", 1500.0, 1850.0],
            ["Kenwood", 1150.0, 1350.0],
            ["Lincoln Park", 3000.0, 3900.0],
        ]

        self.assertEqual(rows, correct_rows)
    
    def test_rent_main_zipcode_level(self):
        """
        Tests rows of main data table for a zipcode-level query, without any
        missing data. Aggregation computes the mean across tracts.
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
            [60601, 2000.0, 2150.0],
            [60602, 1750.0, 1950.0],
            [60603, 1900.0, 3000.0],
        ]

        self.assertEqual(rows, correct_rows)
    
    def test_rent_main_tract_level(self):
        """
        Tests rows of main data table for a tract-level query, without any
        missing data. Aggregation computes the mean across tracts.
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
            [80400, 1000.0, 1500.0],
            [80401, 2000.0, 2200.0],
            [80402, 3000.0, 5000.0],
            [80403, 3000.0, 2800.0],
            [80404, 1500.0, 1700.0],
            [80405, 800.0, 1000.0],
        ]

        self.assertEqual(rows, correct_rows)

    def test_pop_main_city_level(self):
        """
        Tests rows of main data table for a city-level query, with
        missing data. Aggregation computes the sum across tracts.
        """
        geographic_level = "City of Chicago"
        geographic_unit = []
        indicator = "Total Population and Race Group"
        model = Races_Main
        periods = PERIOD_LIST

        rows = MainTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).table["rows"]
        
        correct_rows = [
            ["City Total", 105000.0, 115000.0],
        ]

        self.assertEqual(rows, correct_rows)
    
    def test_pop_main_community_level(self):
        """
        Tests rows of main data table for a community-level query, with
        missing data. Aggregation computes the sum across tracts.
        """
        geographic_level = "Community"
        geographic_unit = COMMUNTIY_LIST
        indicator = "Total Population and Race Group"
        model = Races_Main
        periods = PERIOD_LIST

        rows = MainTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).table["rows"]
        
        correct_rows = [
            ["Hyde Park", 30000.0, 37000.0],
            ["Kenwood", 15000.0, "NA"],
            ["Lincoln Park", 60000.0, 78000.0],
        ]

        self.assertEqual(rows, correct_rows)
    
    def test_pop_main_zipcode_level(self):
        """
        Tests rows of main data table for a zipcode-level query, with
        missing data. Aggregation computes the sum across tracts.
        """
        geographic_level = "Zipcode"
        geographic_unit = ZIPCODE_LIST
        indicator = "Total Population and Race Group"
        model = Races_Main
        periods = PERIOD_LIST

        rows = MainTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).table["rows"]
        
        correct_rows = [
            [60601, 40000.0, 43000.0],
            [60602, 35000.0, 22000.0],
            [60603, 30000.0, 50000.0],
        ]

        self.assertEqual(rows, correct_rows)
    
    def test_pop_main_tract_level(self):
        """
        Tests rows of main data table for a tract-level query, with
        missing data.
        """
        geographic_level = "Tract"
        geographic_unit = TRACT_LIST
        indicator = "Total Population and Race Group"
        model = Races_Main
        periods = PERIOD_LIST

        rows = MainTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).table["rows"]
        
        correct_rows = [
            [80400, 10000.0, 15000.0],
            [80401, 20000.0, 22000.0],
            [80402, 30000.0, 50000.0],
            [80403, 30000.0, 28000.0],
            [80404, 15000.0, "NA"],
            [80405, "NA", "NA"],
        ]

        self.assertEqual(rows, correct_rows)


class CreateSubgroupTableTests(TestCase):
    """
    Tests the SubgroupTable class in utils.py that is required to create the
    subgorup data tables in the web app.
    """
    def setUp(self):

        # 6 Census Tracts, 3 Zipcodes, 3 Neighborhoods
        CensusTracts.objects.create(tract_id=80400, community="HYDE PARK")
        CensusTracts.objects.create(tract_id=80401, community="HYDE PARK")
        CensusTracts.objects.create(tract_id=80402, community="LINCOLN PARK")
        CensusTracts.objects.create(tract_id=80403, community="LINCOLN PARK")
        CensusTracts.objects.create(tract_id=80404, community="KENWOOD")
        CensusTracts.objects.create(tract_id=80405, community="KENWOOD")

        TractZipCode.objects.create(id=1, tract_id=80400, zip_code=60601)
        TractZipCode.objects.create(id=2, tract_id=80401, zip_code=60602)
        TractZipCode.objects.create(id=3, tract_id=80402, zip_code=60603)
        TractZipCode.objects.create(id=4, tract_id=80403, zip_code=60601)
        TractZipCode.objects.create(id=5, tract_id=80404, zip_code=60602)
        TractZipCode.objects.create(id=6, tract_id=80405, zip_code=60603)

        # Indicator 1 - "Aggregate Contract Rent" (No Missing Data)
        # Aggregation takes the average values across tracts
        subgroup_1_a = "lower_rent"
        subgroup_1_b = "upper_rent"
    
        ContractRent_Sub.objects.create(
            id=1,
            indicator_id=4,
            sub_group_indicator_name=subgroup_1_a,
            census_tract_id=80400,
            year=2017,
            value=1000
        )
        ContractRent_Sub.objects.create(
            id=2,
            indicator_id=4,
            sub_group_indicator_name=subgroup_1_b,
            census_tract_id=80400,
            year=2017,
            value=1500
        )
        ContractRent_Sub.objects.create(
            id=3,
            indicator_id=4,
            sub_group_indicator_name=subgroup_1_a,
            census_tract_id=80401,
            year=2017,
            value=1300
        )
        ContractRent_Sub.objects.create(
            id=4,
            indicator_id=4,
            sub_group_indicator_name=subgroup_1_b,
            census_tract_id=80401,
            year=2017,
            value=2000
        )
        ContractRent_Sub.objects.create(
            id=5,
            indicator_id=4,
            sub_group_indicator_name=subgroup_1_a,
            census_tract_id=80402,
            year=2017,
            value=800
        )
        ContractRent_Sub.objects.create(
            id=6,
            indicator_id=4,
            sub_group_indicator_name=subgroup_1_b,
            census_tract_id=80402,
            year=2017,
            value=1100
        )
        ContractRent_Sub.objects.create(
            id=7,
            indicator_id=4,
            sub_group_indicator_name=subgroup_1_a,
            census_tract_id=80403,
            year=2017,
            value=1000
        )
        ContractRent_Sub.objects.create(
            id=8,
            indicator_id=4,
            sub_group_indicator_name=subgroup_1_b,
            census_tract_id=80403,
            year=2017,
            value=2000
        )
        ContractRent_Sub.objects.create(
            id=9,
            indicator_id=4,
            sub_group_indicator_name=subgroup_1_a,
            census_tract_id=80404,
            year=2017,
            value=3000
        )
        ContractRent_Sub.objects.create(
            id=10,
            indicator_id=4,
            sub_group_indicator_name=subgroup_1_b,
            census_tract_id=80404,
            year=2017,
            value=5000
        )
        ContractRent_Sub.objects.create(
            id=11,
            indicator_id=4,
            sub_group_indicator_name=subgroup_1_a,
            census_tract_id=80405,
            year=2017,
            value=5500
        )
        ContractRent_Sub.objects.create(
            id=12,
            indicator_id=4,
            sub_group_indicator_name=subgroup_1_b,
            census_tract_id=80405,
            year=2017,
            value=6500
        )

        # Indicator 2 - "Total Population and Race Group" (With Missing Data)
        # Aggregation takes the sum of values across tracts
        # Tract 80402 does not have subgroup 2a
        # Tract 80403 does not have subgroup 2b
        subgroup_2_a = "pop_asia"
        subgroup_2_b = "pop_white"
        Races_Sub.objects.create(
            id=1,
            indicator_id=5,
            sub_group_indicator_name=subgroup_2_a,
            census_tract_id=80400,
            year=2017,
            value=10000
        )
        Races_Sub.objects.create(
            id=2,
            indicator_id=5,
            sub_group_indicator_name=subgroup_2_b,
            census_tract_id=80400,
            year=2017,
            value=15000
        )
        Races_Sub.objects.create(
            id=3,
            indicator_id=5,
            sub_group_indicator_name=subgroup_2_a,
            census_tract_id=80401,
            year=2017,
            value=13000
        )
        Races_Sub.objects.create(
            id=4,
            indicator_id=5,
            sub_group_indicator_name=subgroup_2_b,
            census_tract_id=80401,
            year=2017,
            value=20000
        )
        Races_Sub.objects.create(
            id=5,
            indicator_id=5,
            sub_group_indicator_name=subgroup_2_a,
            census_tract_id=80402,
            year=2017,
            value=None
        )
        Races_Sub.objects.create(
            id=6,
            indicator_id=5,
            sub_group_indicator_name=subgroup_2_b,
            census_tract_id=80402,
            year=2017,
            value=11000
        )
        Races_Sub.objects.create(
            id=7,
            indicator_id=5,
            sub_group_indicator_name=subgroup_2_a,
            census_tract_id=80403,
            year=2017,
            value=10000
        )
        Races_Sub.objects.create(
            id=8,
            indicator_id=5,
            sub_group_indicator_name=subgroup_2_b,
            census_tract_id=80403,
            year=2017,
            value=None
        )
        Races_Sub.objects.create(
            id=9,
            indicator_id=5,
            sub_group_indicator_name=subgroup_2_a,
            census_tract_id=80404,
            year=2017,
            value=30000
        )
        Races_Sub.objects.create(
            id=10,
            indicator_id=5,
            sub_group_indicator_name=subgroup_2_b,
            census_tract_id=80404,
            year=2017,
            value=50000
        )
        Races_Sub.objects.create(
            id=11,
            indicator_id=5,
            sub_group_indicator_name=subgroup_2_a,
            census_tract_id=80405,
            year=2017,
            value=55000
        )
        Races_Sub.objects.create(
            id=12,
            indicator_id=5,
            sub_group_indicator_name=subgroup_2_b,
            census_tract_id=80405,
            year=2017,
            value=65000
        )
    
    def test_rent_sub_city_level(self):
        """
        Tests rows of subgroup data table for a city-level query, without 
        any missing data. Aggregation computes the mean across tracts.
        """
        geographic_level = "City of Chicago"
        geographic_unit = []
        indicator = "Aggregate Contract Rent"
        model = ContractRent_Sub
        periods = SINGLE_PERIOD_LIST

        rows = SubgroupTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).many_subtables[SINGLE_PERIOD_LIST[0]]["rows"]
        
        correct_rows = [
            ["Lower Contract Rent Quartile", 2100.0],
            ["Upper Contract Rent Quartile", 3016.67],
        ]

        self.assertEqual(rows, correct_rows)
    
    def test_rent_sub_community_level(self):
        """
        Tests rows of subgroup data table for a community-level query, without 
        any missing data. Aggregation computes the mean across tracts.
        """
        geographic_level = "Community"
        geographic_unit = COMMUNTIY_LIST
        indicator = "Aggregate Contract Rent"
        model = ContractRent_Sub
        periods = SINGLE_PERIOD_LIST

        rows = SubgroupTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).many_subtables[SINGLE_PERIOD_LIST[0]]["rows"]
        
        correct_rows = [
            ["Lower Contract Rent Quartile", 1150.0, 900.0, 4250.0],
            ["Upper Contract Rent Quartile", 1750.0, 1550.0, 5750.0],
        ]

        self.assertEqual(rows, correct_rows)
    
    def test_rent_sub_zipcode_level(self):
        """
        Tests rows of subgroup data table for a zipcode-level query, without 
        any missing data. Aggregation computes the mean across tracts.
        """
        geographic_level = "Zipcode"
        geographic_unit = ZIPCODE_LIST
        indicator = "Aggregate Contract Rent"
        model = ContractRent_Sub
        periods = SINGLE_PERIOD_LIST

        rows = SubgroupTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).many_subtables[SINGLE_PERIOD_LIST[0]]["rows"]
        
        correct_rows = [
            ["Lower Contract Rent Quartile", 1000.0, 2150.0, 3150.0],
            ["Upper Contract Rent Quartile", 1750.0, 3500.0, 3800.0],
        ]

        self.assertEqual(rows, correct_rows)

    def test_pop_sub_city_level(self):
        """
        Tests rows of subgroup data table for a city-level query, with
        missing data. Aggregation computes the sum across tracts.
        """
        geographic_level = "City of Chicago"
        geographic_unit = []
        indicator = "Total Population and Race Group"
        model = Races_Sub
        periods = SINGLE_PERIOD_LIST

        rows = SubgroupTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).many_subtables[SINGLE_PERIOD_LIST[0]]["rows"]
        
        correct_rows = [
            ["Asian", 118000.0],
            ["White", 161000.0],
        ]

        self.assertEqual(rows, correct_rows)
    
    def test_pop_sub_community_level(self):
        """
        Tests rows of subgroup data table for a community-level query, with
        missing data. Aggregation computes the sum across tracts.
        """
        geographic_level = "Community"
        geographic_unit = COMMUNTIY_LIST
        indicator = "Total Population and Race Group"
        model = Races_Sub
        periods = SINGLE_PERIOD_LIST

        rows = SubgroupTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).many_subtables[SINGLE_PERIOD_LIST[0]]["rows"]
        
        correct_rows = [
            ["Asian", 23000, 10000, 85000],
            ["White", 35000, 11000, 115000],
        ]

        self.assertEqual(rows, correct_rows)
    
    def test_pop_sub_zipcode_level(self):
        """
        Tests rows of subgroup data table for a zipcode-level query, with
        missing data. Aggregation computes the sum across tracts.
        """
        geographic_level = "Zipcode"
        geographic_unit = ZIPCODE_LIST
        indicator = "Total Population and Race Group"
        model = Races_Sub
        periods = SINGLE_PERIOD_LIST

        rows = SubgroupTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).many_subtables[SINGLE_PERIOD_LIST[0]]["rows"]
        
        correct_rows = [
            ["Asian", 20000.0, 43000.0, 55000.0],
            ["White", 15000.0, 70000.0, 76000.0],
        ]

        self.assertEqual(rows, correct_rows)


class TestHeatmaps(TestCase):
    def test_heatmaps(self):
        """
        Tests heatmap generation function in utils.py
        """

        geographic_level = "Community"
        indicator = "Aggregate Contract Rent"
        field = {
            "headers": ["Community", "2017", "2018"],
            "rows": [
                ["HYDE PARK", 1500, 1850],
                ["LINCOLN PARK", 3000, 3900],
                ["KENWOOD", 1150, 1350],
            ]
        }
        years = ["2017", "2018"]
        heatmap_data, heatmap_info = generate_heatmaps(geographic_level, 
                                                       indicator, field, years)
        self.assertIsNotNone(heatmap_data)
        self.assertEqual(len(heatmap_info), 2)

class TestWriteMemo(TestCase):
    def test_write_memo(self):
        """
        Tests the WriteMemo class in utils.py.
        """
        indicator = "Aggregate Contract Rent"
        geo_level = "Community"
        dictionary = {
            "headers": ["Community", "2017", "2018"],
            "rows": [
                ["HYDE PARK", 1500, 1850],
                ["LINCOLN PARK", 3000, 3900],
                ["KENWOOD", 1150, 1350],
            ]
        }
        data = pd.DataFrame(dictionary["rows"], columns=dictionary["headers"])
        describe = data.describe()

        memo_generator = WriteMemo(indicator, geo_level, dictionary, describe, 
                                   open_ai_key)

        memo_text = memo_generator.invoke()

        self.assertIsNotNone(memo_text)
        self.assertIsInstance(memo_text, str)

class TestMainChartViz(TestCase):
    def test_visualization_rendering(self):
        """
        Tests the visualization chart for the main indicator data table.
        """
        chart_data = {
            'categories': ['Category 1', 'Category 2', 'Category 3'],
            'series': [
                {'name': 'Series 1', 'data': [1, 2, 3]},
                {'name': 'Series 2', 'data': [4, 5, 6]},
                {'name': 'Series 3', 'data': [7, 8, 9]}
            ]
        }
        table_title = 'Main Chart'

        template_string = '''
        <script>
            document.addEventListener('DOMContentLoaded', function () {
                var chartData = {{ chart_data | safe }};
                var currentView = 'category';
                
                        function updateMainChart() {
                            var categories = chartData.categories;
                            var series = chartData.series;

                            var seriesData;

                            if (currentView === 'category') {
                                seriesData = series;
                            } else {
                                seriesData = categories.map(function(category, index) {
                                    var categoryData = series.map(function(serie) {
                                        return serie.data[index];
                                    });

                                    return {
                                        name: category,
                                        data: categoryData
                                    };
                                });
                            }

                            var chartOptions = {
                                chart: {
                                    type: 'bar'
                                },
                                title: {
                                    text: '{{ table_title }}'
                                },
                                xAxis: {
                                    categories: currentView === 'category' ? categories : series.map(function(serie) {
                                        return serie.name;
                                    })
                                },
                                yAxis: {
                                    min: 0,
                                    title: {
                                        text: 'Value'
                                    }
                                },
                                legend: {
                                    reversed: true
                                },
                                plotOptions: {
                                    series: {
                                        stacking: 'normal'
                                    }
                                },
                                series: seriesData
                            };

                            Highcharts.chart('chart-container', chartOptions);
                        }

                        updateMainChart();

                        document.getElementById('toggle-main-view').addEventListener('click', function() {
                            currentView = currentView === 'category' ? 'series' : 'category';
                            updateMainChart();
                });
            });
        </script>
        '''
    
        template = Template(template_string)
        context = Context({'chart_data': chart_data, 'table_title': table_title})
        rendered_js = template.render(context)
        
        self.assertIn('var chartData = ', rendered_js)
        self.assertIn('var currentView = \'category\';', rendered_js)
        self.assertIn('function updateMainChart()', rendered_js)
        self.assertIn('updateMainChart();', rendered_js)
        self.assertIn('document.getElementById(\'toggle-main-view\').addEventListener(\'click\', function()', rendered_js)

if __name__ == '__main__':
    unittest.main(verbosity=2)
