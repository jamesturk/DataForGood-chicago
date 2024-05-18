from django.test import TestCase

from .models import CensusTracts, TractZipCode
from .utils import (
    MAIN_MODEL_MAPPING,
    create_table,
)


INDICATORS_LIST = list(MAIN_MODEL_MAPPING.keys())

TRACT_LIST = [
    tup[0]
    for tup in list(TractZipCode.objects.values_list("tract_id").distinct())
]

ZIPCODE_LIST = [
    tup[0]
    for tup in list(TractZipCode.objects.values_list("zip_code").distinct())
]

COMMUNITY_LST = [
    tup[0]
    for tup in list(CensusTracts.objects.values_list("community").distinct())
]

PERIOD_LIST = [
    "2013-2017",
    "2014-2018",
    "2015-2019",
    "2016-2020",
    "2017-2021",
    "2018-2022",
]


class CreateMainTableTests(TestCase):
    """
    Tests the create_table() function in utils.py that is required to create the
    main data table in the web app.
    """

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

        for indicator in INDICATORS_LIST:
            rows = create_table(
                geographic_level, geographic_unit, indicator, periods
            )["rows"]
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

        for indicator in INDICATORS_LIST:
            rows = create_table(
                geographic_level, geographic_unit, indicator, periods
            )["rows"]
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

        for indicator in INDICATORS_LIST:
            rows = create_table(
                geographic_level, geographic_unit, indicator, periods
            )["rows"]
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

        for indicator in INDICATORS_LIST:
            rows = create_table(
                geographic_level, geographic_unit, indicator, periods
            )["rows"]
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

        for indicator in INDICATORS_LIST:
            rows = create_table(
                geographic_level, geographic_unit, indicator, periods
            )["rows"]
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

        for indicator in INDICATORS_LIST:
            rows = create_table(
                geographic_level, geographic_unit, indicator, periods
            )["rows"]
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

        for indicator in INDICATORS_LIST:
            rows = create_table(
                geographic_level, geographic_unit, indicator, periods
            )["rows"]
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

        for indicator in INDICATORS_LIST:
            rows = create_table(
                geographic_level, geographic_unit, indicator, periods
            )["rows"]
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

        for indicator in INDICATORS_LIST:
            rows = create_table(
                geographic_level, geographic_unit, indicator, periods
            )["rows"]
            self.assertIs(len(rows) == len(geographic_unit), True)

    def test_community_table_check_for_none(self):
        """
        Tests that the None value is not included in table rows. All queries
        instances that are None values should have been converted to the "NA"
        string. Testing at Community level, for all communities and all periods
        available in the database, for all indicators.
        """
        geographic_level = "Community"
        geographic_unit = COMMUNITY_LST
        periods = PERIOD_LIST

        for indicator in INDICATORS_LIST:
            rows = create_table(
                geographic_level, geographic_unit, indicator, periods
            )["rows"]
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
        geographic_unit = COMMUNITY_LST
        periods = PERIOD_LIST

        for indicator in INDICATORS_LIST:
            rows = create_table(
                geographic_level, geographic_unit, indicator, periods
            )["rows"]
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
        geographic_unit = COMMUNITY_LST
        periods = PERIOD_LIST

        for indicator in INDICATORS_LIST:
            rows = create_table(
                geographic_level, geographic_unit, indicator, periods
            )["rows"]
            self.assertIs(len(rows) == len(geographic_unit), True)
