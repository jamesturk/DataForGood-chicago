import csv
import os

from django.apps import apps
from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = "Load data from CSV files into the database"

    def handle(self, *args, **kwargs):
        """
        Handle the command to load data from CSVs into the database.

        The function sets the base directory for the CSV files and calls
        methods to load specific datasets and other model data.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        base_dir = os.path.join(
            settings.BASE_DIR,
            os.path.pardir,
            "dfg_chi/backend/data_downloaded/Agg_data",
        )

        # Process tracts and zipcode files
        self.load_census_tracts_data(os.path.join(base_dir, "CensusTracts.csv"))
        self.load_tract_zip_codes_data(
            os.path.join(base_dir, "TractZipCodes.csv")
        )

        # Process other files
        for filename in os.listdir(base_dir):
            if filename.endswith(".csv") and filename not in [
                "CensusTracts.csv",
                "TractZipCodes.csv",
            ]:
                self.load_model_data(base_dir, filename)

    def load_model_data(self, base_dir, filename):
        """
        Load indicator data from a CSV into the corresponding Django model.

        This function dynamically loads data into a model based on the
        filename. It assumes the model name matches the CSV filename
        without the extension.

        Args:
            base_dir (str): The base directory where the CSV file is located.
            filename (str): The name of the CSV.
        """
        model_name = filename.replace(".csv", "")
        try:
            model = apps.get_model("main", model_name)
            self.stdout.write(f"Loading data into model: {model_name}")
            with transaction.atomic():
                self.load_data(model, os.path.join(base_dir, filename))
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully loaded data into {model_name}"
                )
            )
        except LookupError:
            self.stdout.write(
                self.style.ERROR(f"No model found for {model_name}")
            )

    def load_census_tracts_data(self, file_path):
        """
        Load census tracts data from CSV into the CensusTracts model.

        Args:
            file_path (str): The path to the CSV containing census tracts data.
        """
        model = apps.get_model("main", "CensusTracts")
        with open(file_path, newline="") as file:
            reader = csv.DictReader(file)
            instances = []
            for record in reader:
                try:
                    instance = model(**record)
                    instances.append(instance)
                except IntegrityError as e:
                    self.stdout.write(
                        self.style.ERROR(f"Error saving record: {str(e)}")
                    )
                    continue
            model.objects.bulk_create(instances, ignore_conflicts=True)
            self.stdout.write(
                self.style.SUCCESS("Successfully loaded data into CensusTracts")
            )

    def load_tract_zip_codes_data(self, file_path):
        """
        Load zipcodes data from CSV into the TractZipCode model and handles
        foreign key associations by looking up related CensusTracts instances.

        Args:
            file_path (str): The path to the CSV containing zipcodes data.
        """
        TractModel = apps.get_model("main", "CensusTracts")
        ZipCodeModel = apps.get_model("main", "TractZipCode")
        with open(file_path, newline="") as file:
            reader = csv.DictReader(file)
            instances = []
            for record in reader:
                try:
                    # Retrieve the Tract object using tract_id from CSV
                    tract = TractModel.objects.get(
                        tract_id=int(record["tract_id"])
                    )
                    # Create an instance of TractZipCode with the correct ForeignKey association
                    zip_code_instance = ZipCodeModel(
                        tract=tract, zip_code=int(record["zip_code"])
                    )
                    instances.append(zip_code_instance)
                except TractModel.DoesNotExist:
                    self.stdout.write(
                        self.style.ERROR(
                            f"Census tract not found for ID {record['tract_id']}"
                        )
                    )
                    continue
                except IntegrityError as e:
                    self.stdout.write(
                        self.style.ERROR(f"Error saving record: {str(e)}")
                    )
                    continue
                except ValueError as e:
                    self.stdout.write(
                        self.style.ERROR(f"Data conversion error: {str(e)}")
                    )
                    continue
            # Bulk create all the gathered instances to the database
            ZipCodeModel.objects.bulk_create(instances, ignore_conflicts=True)
            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully loaded data into TractZipCodes"
                )
            )

    def load_data(self, model, file_path):
        """
        Load (general) indicators data from a CSV into the specified model.

        Args:
            model (Model): The Django model class to load data into.
            file_path (str): The path to the CSV file containing the data.
        """
        with open(file_path, newline="") as file:
            reader = csv.DictReader(file)
            instances = []
            for record in reader:
                cleaned_record = {
                    k: (None if v == "" else v) for k, v in record.items()
                }
                try:
                    instance = model(**cleaned_record)
                    instances.append(instance)
                except ValueError as e:
                    self.stdout.write(
                        self.style.ERROR(f"Error parsing record: {str(e)}")
                    )
                    continue
            model.objects.bulk_create(instances, ignore_conflicts=True)
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully loaded data into {model.__name__}"
                )
            )
