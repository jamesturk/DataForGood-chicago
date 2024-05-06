from django.db import models

# Create your models here.
class Georeference(models.Model):
    # Primary Key (Georeference ID - i.e. Tract Number)
    id = models.IntegerField(primary_key=True)
    zip_code = models.IntegerField(default=999999)
    community_name = models.CharField(max_length=50)

    def __str__(self):
        """
        """
        return str(self.id) + " " + str(self.zip_code) + " " + self.community_name

class EconomicMain(models.Model):
    # UID (unqiue row numbers auto increment)
    uid = models.AutoField(primary_key=True)

    # Indicator ID (ID for each EconomicMain indicator)
    indicator_id = models.IntegerField(default=1)
    # Foreign Key (Georeference ID - i.e. Tract Number)
    georeference_id = models.ForeignKey(Georeference, on_delete=models.CASCADE)

    indicator_name = models.CharField(max_length=50)
    year = models.IntegerField(default=9999)
    value = models.IntegerField(default=9999)

    def __str__(self):
        """
        """
        return str(self.georeference_id) + " " + self.indicator_name + " " + str(self.year) + " " + str(self.value)

class EconomicSub(models.Model):
    # UID (unique row numbers auto increment)
    uid = models.AutoField(primary_key=True)

    # Foreign Key 1 (Georereference ID)
    georeference_id = models.ForeignKey(Georeference, on_delete=models.CASCADE)
    # Foreign Key 2 (ID for an EconomicMain indicator)
    indicator_id = models.ForeignKey(EconomicMain, on_delete=models.CASCADE)

    subgroup_indicator_name = models.CharField(max_length=50)
    year = models.IntegerField(default=9999)
    value = models.IntegerField(default=9999)

    def __str__(self):
        """
        """
        return str(self.indicator_id) + " " + self.subgroup_indicator_name + " " + str(self.year) + " " + str(self.value)