from django.contrib import admin

from model_hris.performance_management.models import (
    Rating_Accomplishment,
    Accomplishment,
    Success_Indicator,
    Year,
)

admin.site.register(Rating_Accomplishment)
admin.site.register(Accomplishment)
admin.site.register(Success_Indicator)
admin.site.register(Year)
