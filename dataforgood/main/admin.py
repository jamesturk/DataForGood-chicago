from django.contrib import admin

# Register your models here.
from .models import EconomicMain, EconomicSub, Georeference


admin.site.register(Georeference)
admin.site.register(EconomicMain)
admin.site.register(EconomicSub)
