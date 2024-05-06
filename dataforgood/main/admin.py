from django.contrib import admin

# Register your models here.
from .models import Georeference, EconomicMain, EconomicSub

admin.site.register(Georeference)
admin.site.register(EconomicMain)
admin.site.register(EconomicSub)