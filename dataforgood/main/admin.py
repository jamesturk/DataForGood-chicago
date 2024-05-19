from django.contrib import admin

# Register your models here.
from .models import CensusTracts, ContractRent_Main, ContractRent_Sub


admin.site.register(CensusTracts)
admin.site.register(ContractRent_Main)
admin.site.register(ContractRent_Sub)
