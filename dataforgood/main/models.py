from django.db import models

class CensusTracts(models.Model):
    tract_id = models.IntegerField(primary_key=True)
    community = models.CharField(max_length=255)

class TractZipCode(models.Model):
    id = models.AutoField(primary_key=True)
    tract = models.ForeignKey(CensusTracts,
                              on_delete=models.CASCADE,
                              related_name='zip_codes')
    zip_code = models.IntegerField()

    def __str__(self):
        return f"{self.tract.tract_id} - {self.zip_code}"


class BaseIndicator(models.Model):
    id = models.AutoField(primary_key=True)
    indicator_id = models.IntegerField()
    census_tract = models.ForeignKey(CensusTracts,
                                    on_delete=models.CASCADE)
    year = models.IntegerField()
    value = models.IntegerField()

    class Meta:
        abstract = True

class MainIndicator(BaseIndicator):
    indicator_name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.indicator_name

class SubIndicator(BaseIndicator):
    sub_group_indicator_name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.sub_group_indicator_name

class ContractRent_Main(MainIndicator):
    pass

class ContractRent_Sub(SubIndicator):
    pass

class Disability_Main(MainIndicator):
    pass

class Disability_Sub(SubIndicator):
    pass

class Enrollment_Main(MainIndicator):
    pass

class Enrollment_Sub(SubIndicator):
    pass

class HouseholdType_Main(MainIndicator):
    pass

class HouseholdType_Sub(SubIndicator):
    pass

class Insurance_Main(MainIndicator):
    pass

class Insurance_Sub(SubIndicator):
    pass

class MeanIncome_Main(MainIndicator):
    pass

class MeanIncome_Sub(SubIndicator):
    pass

class MedianAge_Main(MainIndicator):
    pass

class MedianAge_Sub(SubIndicator):
    pass

class MedianEarning_Main(MainIndicator):
    pass

class MedianEarning_Sub(SubIndicator):
    pass

class MedianIncome_Main(MainIndicator):
    pass

class MedianIncome_Sub(SubIndicator):
    pass

class Races_Main(MainIndicator):
    pass

class Races_Sub(SubIndicator):
    pass