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
            value=1000
        )
        Races_Main.objects.create(
            id=2,
            sub_group_indicator_name=indicator_name,
            census_tract=80400,
            year=2018,
            value=1500
        )
        Races_Main.objects.create(
            id=3,
            sub_group_indicator_name=indicator_name,
            census_tract=80401,
            year=2017,
            value=2000
        )
        Races_Main.objects.create(
            id=4,
            sub_group_indicator_name=indicator_name,
            census_tract=80401,
            year=2018,
            value=2200
        )
        Races_Main.objects.create(
            id=5,
            sub_group_indicator_name=indicator_name,
            census_tract=80402,
            year=2017,
            value=3000
        )
        Races_Main.objects.create(
            id=6,
            sub_group_indicator_name=indicator_name,
            census_tract=80402,
            year=2018,
            value=5000
        )
        Races_Main.objects.create(
            id=7,
            sub_group_indicator_name=indicator_name,
            census_tract=80403,
            year=2017,
            value=3000
        )
        Races_Main.objects.create(
            id=8,
            sub_group_indicator_name=indicator_name,
            census_tract=80403,
            year=2018,
            value=2800
        )
        Races_Main.objects.create(
            id=9,
            sub_group_indicator_name=indicator_name,
            census_tract=80404,
            year=2017,
            value=1500
        )

    def test_city_table_check_for_none(self):
        """
        Tests that the None value is not included in table rows. All queries
        instances that are None values should have been converted to the "NA"
        string. Testing at the city level for all periods available in the
        database, for all indicators.
        """
        geographic_level = "City of Chicago"
        geographic_unit = []
        periods = PERIOD_LIST

        for indicator, model in zip(INDICATORS_LIST, 
                                    [ContractRent_Main, Races_Main]):
            rows = MainTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).table["rows"]
            for row in rows:
                self.assertIs(None in row, False)

    def test_city_table_row_length(self):
        """
        Testing that the number of items in a row is equal to the number of
        periods selected by the user, because each column represents a period.
        If data for a given period does not exist for a tract in the database,
        a "NA" string should be used as a placeholder for that column. Testing
        at the city level, for all periods available in the database, for all
        indicators.
        """
        geographic_level = "City of Chicago"
        geographic_unit = []
        periods = PERIOD_LIST

        for indicator, model in zip(INDICATORS_LIST, 
                                    [ContractRent_Main, Races_Main]):
            rows = MainTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).table["rows"]
            for row in rows:
                self.assertI(len(row) == len(periods), True)

    def test_city_table_num_rows(self):
        """
        Testing that the number of rows is equal to one for city level data.
        Testing at the city level, for all periods available in the database,
        for all indicators.
        """
        geographic_level = "City of Chicago"
        geographic_unit = []
        periods = PERIOD_LIST

        for indicator, model in zip(INDICATORS_LIST, 
                                    [ContractRent_Main, Races_Main]):
            rows = MainTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).table["rows"]
        self.assertIs(len(rows) == 1, True)

    def test_tract_table_check_for_none(self):
        """
        Tests that the None value is not included in table rows. All queries
        instances that are None values should have been converted to the "NA"
        string. Testing at the Tract level, for all tracts and all periods
        available in the database, for all indicators.
        """
        geographic_level = "Tract"
        geographic_unit = TRACT_LIST
        periods = PERIOD_LIST

        for indicator, model in zip(INDICATORS_LIST, 
                                    [ContractRent_Main, Races_Main]):
            rows = MainTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).table["rows"]
            for row in rows:
                self.assertIs(None in row, False)

    def test_tract_table_row_length(self):
        """
        Testing that the number of items in a row is equal to the number of
        periods selected by the user, because each column represents a period.
        If data for a given period does not exist for a tract in the database,
        a "NA" string should be used as a placeholder for that column. Testing
        at the Tract level, for all tracts and all periods available in the
        database, for all indicators.
        """
        geographic_level = "Tract"
        geographic_unit = TRACT_LIST
        periods = PERIOD_LIST

        for indicator, model in zip(INDICATORS_LIST, 
                                    [ContractRent_Main, Races_Main]):
            rows = MainTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).table["rows"]
            for row in rows:
                self.assertI(len(row) == len(periods), True)

    def test_tract_table_num_rows(self):
        """
        Testing that the  number of rows is equal to the number of geographic
        units (i.e. tracts) selected by the user because each row represents
        data for a given tract. Testing at the Tract level, for all tracts and
        all periods available in the database, for all indicators.
        """
        geographic_level = "Tract"
        geographic_unit = TRACT_LIST
        periods = PERIOD_LIST

        for indicator, model in zip(INDICATORS_LIST, 
                                    [ContractRent_Main, Races_Main]):
            rows = MainTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).table["rows"]
            self.assertIs(len(rows) == len(geographic_unit), True)

    def test_zipcode_table_check_for_none(self):
        """
        Tests that the None value is not included in table rows. All queries
        instances that are None values should have been converted to the "NA"
        string. Testing at the Zipcode level, for all zipcodes and all periods
        available in the database, for all indicators.
        """
        geographic_level = "Zipcode"
        geographic_unit = ZIPCODE_LIST
        periods = PERIOD_LIST

        for indicator, model in zip(INDICATORS_LIST, 
                                    [ContractRent_Main, Races_Main]):
            rows = MainTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).table["rows"]
            for row in rows:
                self.assertIs(None in row, False)

    def test_zipcode_table_row_length(self):
        """
        Testing that the number of items in a row is equal to the number of
        periods selected by the user, because each column represents a period.
        If data for a given period does not exist for a tract in the database,
        a "NA" string should be used as a placeholder for that column. Testing
        at the Zipcode level, for all zipcodes and all periods available in the
        database, for all indicators.
        """
        geographic_level = "Zipcode"
        geographic_unit = ZIPCODE_LIST
        periods = PERIOD_LIST

        for indicator, model in zip(INDICATORS_LIST, 
                                    [ContractRent_Main, Races_Main]):
            rows = MainTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).table["rows"]
            for row in rows:
                self.assertIs(len(row) == len(periods), True)

    def test_zipcode_table_num_rows(self):
        """
        Testing that the  number of rows is equal to the number of geographic
        units (i.e. zipcodes) selected by the user because each row represents
        data for a given zipcode. Testing at the Zipcode level, for all zipcodes
        and all periods available in the database, for all indicators.
        """
        geographic_level = "Zipcode"
        geographic_unit = ZIPCODE_LIST
        periods = PERIOD_LIST

        for indicator, model in zip(INDICATORS_LIST, 
                                    [ContractRent_Main, Races_Main]):
            rows = MainTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).table["rows"]
            self.assertIs(len(rows) == len(geographic_unit), True)

    def test_community_table_check_for_none(self):
        """
        Tests that the None value is not included in table rows. All queries
        instances that are None values should have been converted to the "NA"
        string. Testing at Community level, for all communities and all periods
        available in the database, for all indicators.
        """
        geographic_level = "Community"
        geographic_unit = COMMUNTIY_LIST
        periods = PERIOD_LIST

        for indicator, model in zip(INDICATORS_LIST, 
                                    [ContractRent_Main, Races_Main]):
            rows = MainTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).table["rows"]
            for row in rows:
                self.assertIs(None in row, False)

    def test_community_table_row_length(self):
        """
        Testing that the number of items in a row is equal to the number of
        periods selected by the user, because each column represents a period.
        If data for a given period does not exist for a tract in the database,
        a "NA" string should be used as a placeholder for that column. Testing
        at Community level, for all communities and all periods available in the
        database, for all indicators.
        """
        geographic_level = "Community"
        geographic_unit = COMMUNTIY_LIST
        periods = PERIOD_LIST

        for indicator, model in zip(INDICATORS_LIST, 
                                    [ContractRent_Main, Races_Main]):
            rows = MainTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).table["rows"]
            for row in rows:
                self.assertI(len(row) == len(periods), True)

    def test_tract_table_num_rows(self):
        """
        Testing that the  number of rows is equal to the number of geographic
        units (i.e. communities) selected by the user because each row represents
        data for a given community. Testing at the Community level, for all
        communities and all periods available in the database, for all indicators.
        """
        geographic_level = "Community"
        geographic_unit = COMMUNTIY_LIST
        periods = PERIOD_LIST

        for indicator, model in zip(INDICATORS_LIST, 
                                    [ContractRent_Main, Races_Main]):
            rows = MainTable(
            geographic_level, geographic_unit, indicator, model, periods
            ).table["rows"]
            self.assertIs(len(rows) == len(geographic_unit), True)


# class CreateSubgroupTableTests(TestCase):
#     """
#     Tests the SubgroupTable class in utils.py that is required to create the
#     subgroup data tables in the web app.
#     """

#     def test_city_table_check_for_none(self):
#         """
#         Tests that the None value is not included in table rows. All queries
#         instances that are None values should have been converted to the "NA"
#         string. Testing at the city level for all periods available in the
#         database, for all indicators.
#         """
#         geographic_level = "City of Chicago"
#         geographic_unit = []
#         periods = PERIOD_LIST

#         for indicator in INDICATORS_LIST:
#             subgroup_tables = SubgroupTable(
#             geographic_level, geographic_unit, indicator, periods
#             ).many_subtables

#             for one_subgroup_table in subgroup_tables.values():
#                 for row in one_subgroup_table["rows"]:
#                     self.assertIs(None in row, False)
    
#     def test_city_table_row_length(self):
#         """
#         Testing that the number of items/columns in a row is equal to 2. Testing
#         at the city level, for all periods available in the database, for all
#         indicators.
#         """
#         geographic_level = "City of Chicago"
#         geographic_unit = []
#         periods = PERIOD_LIST

#         for indicator in INDICATORS_LIST:
#             subgroup_tables = SubgroupTable(
#             geographic_level, geographic_unit, indicator, periods
#             ).many_subtables

#             for one_subgroup_table in subgroup_tables.values():
#                 for row in one_subgroup_table["rows"]:
#                     self.assertI(len(row) == 2, True)

#     def test_tract_table_check_for_none(self):
#         """
#         Tests that the None value is not included in table rows. All queries
#         instances that are None values should have been converted to the "NA"
#         string. Testing at the tract level for all periods available in the
#         database, for all indicators.
#         """
#         geographic_level = "Tract"
#         geographic_unit = TRACT_LIST
#         periods = PERIOD_LIST

#         for indicator in INDICATORS_LIST:
#             subgroup_tables = SubgroupTable(
#             geographic_level, geographic_unit, indicator, periods
#             ).many_subtables

#             for one_subgroup_table in subgroup_tables.values():
#                 for row in one_subgroup_table["rows"]:
#                     self.assertIs(None in row, False)
    
#     def test_tract_table_row_length(self):
#         """
#         Testing that the number of items in a row is equal to the number of
#         tracts selected by the user, because each column represents a tract.
#         If data for a given tract does not exist for a tract in the database,
#         a "NA" string should be used as a placeholder for that column. Testing
#         at the tract level, for all tracts available in the database, for all
#         indicators.
#         """
#         geographic_level = "Tract"
#         geographic_unit = TRACT_LIST
#         periods = PERIOD_LIST

#         for indicator in INDICATORS_LIST:
#             subgroup_tables = SubgroupTable(
#             geographic_level, geographic_unit, indicator, periods
#             ).many_subtables

#             for one_subgroup_table in subgroup_tables.values():
#                 for row in one_subgroup_table["rows"]:
#                     self.assertI(len(row) == len(geographic_unit), True)
    
#     def test_zipcode_table_check_for_none(self):
#         """
#         Tests that the None value is not included in table rows. All queries
#         instances that are None values should have been converted to the "NA"
#         string. Testing at the zipcode level for all periods available in the
#         database, for all indicators.
#         """
#         geographic_level = "Zipcode"
#         geographic_unit = ZIPCODE_LIST
#         periods = PERIOD_LIST

#         for indicator in INDICATORS_LIST:
#             subgroup_tables = SubgroupTable(
#             geographic_level, geographic_unit, indicator, periods
#             ).many_subtables

#             for one_subgroup_table in subgroup_tables.values():
#                 for row in one_subgroup_table["rows"]:
#                     self.assertIs(None in row, False)
    
#     def test_zipcode_table_row_length(self):
#         """
#         Testing that the number of items in a row is equal to the number of
#         zipcodes selected by the user, because each column represents a zipcode.
#         If data for a given zipcode does not exist for a tract in the database,
#         a "NA" string should be used as a placeholder for that column. Testing
#         at the zipcode level, for all tracts available in the database, for all
#         indicators.
#         """
#         geographic_level = "Zipcode"
#         geographic_unit = ZIPCODE_LIST
#         periods = PERIOD_LIST

#         for indicator in INDICATORS_LIST:
#             subgroup_tables = SubgroupTable(
#             geographic_level, geographic_unit, indicator, periods
#             ).many_subtables

#             for one_subgroup_table in subgroup_tables.values():
#                 for row in one_subgroup_table["rows"]:
#                     self.assertI(len(row) == len(geographic_unit), True)
    
#     def test_community_table_check_for_none(self):
#         """
#         Tests that the None value is not included in table rows. All queries
#         instances that are None values should have been converted to the "NA"
#         string. Testing at the community level for all periods available in the
#         database, for all indicators.
#         """
#         geographic_level = "Community"
#         geographic_unit = COMMUNITY_LST
#         periods = PERIOD_LIST

#         for indicator in INDICATORS_LIST:
#             subgroup_tables = SubgroupTable(
#             geographic_level, geographic_unit, indicator, periods
#             ).many_subtables

#             for one_subgroup_table in subgroup_tables.values():
#                 for row in one_subgroup_table["rows"]:
#                     self.assertIs(None in row, False)
    
#     def test_community_table_row_length(self):
#         """
#         Testing that the number of items in a row is equal to the number of
#         community selected by the user, because each column represents a community.
#         If data for a given community does not exist for a tract in the database,
#         a "NA" string should be used as a placeholder for that column. Testing
#         at the community level, for all tracts available in the database, for 
#         all indicators.
#         """
#         geographic_level = "Community"
#         geographic_unit = COMMUNITY_LST
#         periods = PERIOD_LIST

#         for indicator in INDICATORS_LIST:
#             subgroup_tables = SubgroupTable(
#             geographic_level, geographic_unit, indicator, periods
#             ).many_subtables

#             for one_subgroup_table in subgroup_tables.values():
#                 for row in one_subgroup_table["rows"]:
#                     self.assertI(len(row) == len(geographic_unit), True)
