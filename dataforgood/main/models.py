from django.db import models


class CensusTracts(models.Model):
    """
    Django model representing the relationship between census tracts and
    community areas in Chicago

    Attributes:
        tract_id (int): Census Tract ID
        community (str): Community area name
    """

    tract_id = models.IntegerField(primary_key=True)
    community = models.CharField(max_length=255)


class TractZipCode(models.Model):
    """
    Django model representing the relationship between census tracts and
    zip codes in Chicago

    Attributes:
        id (int): Unique identifier for each census tract and zip code pairing
        tract (int): Census Tract ID
        zip_code (int): Zip Code
    """

    id = models.AutoField(primary_key=True)
    tract = models.ForeignKey(
        CensusTracts, on_delete=models.CASCADE, related_name="zip_codes"
    )
    zip_code = models.IntegerField()

    def __str__(self):
        return f"{self.tract.tract_id} - {self.zip_code}"


class BaseIndicator(models.Model):
    """
    Abstract model representing base indicator variables for Census data

    Attributes:
        id (int): Unique identifier for each tract and year
        indicator_id (int): identifier for each broader indicator
            category (Economics, Housing, Population, etc.)
        census_tract (int): Census Tract ID
        year (int): Year that data was collected
        value (int): Value of the indicator
    """

    id = models.AutoField(primary_key=True)
    indicator_id = models.IntegerField()
    census_tract = models.ForeignKey(CensusTracts, on_delete=models.CASCADE)
    year = models.IntegerField()
    value = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True


class MainIndicator(BaseIndicator):
    """
    Abstract model representing the main indicators for the Census data

    Attributes:
        indicator_name (str): name of the indicator
    """

    indicator_name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.indicator_name


class SubIndicator(BaseIndicator):
    """
    Abstract model representing the sub-group indicators for the Census data

    Attributes:
        sub_group_indicator_name (str): name of the sub-group indicator
    """

    sub_group_indicator_name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        """
        String representation of the SubIndicator object

        Returns:
            str: name of the sub-group indicator
        """
        return self.sub_group_indicator_name


# For more details about the indicators used in our project please visit:
# https://docs.google.com/spreadsheets/d/1NjXl797YujIS_1Qd10GlLsODTVHPJCxWFNkgq5Lp32c/edit?usp=sharing


class ContractRent_Main(MainIndicator):
    """Model representing the Aggregate Contract Rent indicator"""

    pass


class ContractRent_Sub(SubIndicator):
    """Model representing the Aggregate Contract Rent by Quartile indicator"""

    pass


class Disability_Main(MainIndicator):
    """Model representing the Total Population with Disability indicator"""

    pass


class Disability_Sub(SubIndicator):
    """Model representing the Total Population with Disability by the
    different types of disabilities indicator"""

    pass


class Enrollment_Main(MainIndicator):
    """Model representing the Population 3 years and over enrolled in School
    indicator"""

    pass


class Enrollment_Sub(SubIndicator):
    """Model representing the Population 3 years and over enrolled in School
    by School Type indicator"""

    pass


class HouseholdType_Main(MainIndicator):
    """Model representing the Total Number of Households indicator"""

    pass


class HouseholdType_Sub(SubIndicator):
    """Model representing the Total Number of Households by Types
    of Households indicator"""

    pass


class Insurance_Main(MainIndicator):
    """Model representing the Insurance Coverage indicator"""

    pass


class Insurance_Sub(SubIndicator):
    """Model representing the Insurance Coverage by Insurance Status
    indicator"""

    pass


class MeanIncome_Main(MainIndicator):
    """Model representing the Mean Income in the Past 12 Months
    (inflation-adjusted) indicator"""

    pass


class MeanIncome_Sub(SubIndicator):
    """Model representing the Mean Income in the Past 12 Months
    (inflation-adjusted) by Race indicator"""

    pass


class MedianAge_Main(MainIndicator):
    """Model representing the Median Age indicator"""

    pass


class MedianAge_Sub(SubIndicator):
    """Model representing the Median Age by Sex indicator"""

    pass


class MedianEarning_Main(MainIndicator):
    """Model representing the Median Earnings in the Past 12 Months
    indicator"""

    pass


class MedianEarning_Sub(SubIndicator):
    """Model representing the Median Earnings in the Past 12 Months by
    Education Level indicator"""

    pass


class MedianIncome_Main(MainIndicator):
    """Model representing the Median Income in the Past 12 Months
    (inflation-adjusted) indicator"""

    pass


class MedianIncome_Sub(SubIndicator):
    """Model representing the Median Income in the Past 12 Months
    (inflation-adjusted) by Race indicator"""

    pass


class Races_Main(MainIndicator):
    """Model representing the Total Population indicator"""

    pass


class Races_Sub(SubIndicator):
    """Model representing the Total Population by Race indicator"""

    pass
