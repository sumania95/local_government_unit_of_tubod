from django.contrib import admin

from .models import (
    Actual_Accomplishment,
    Rating_Accomplishment,
    Accomplishment,
    Success_Indicator,
    Year,
)


admin.site.register(Actual_Accomplishment)
admin.site.register(Rating_Accomplishment)
admin.site.register(Accomplishment)
admin.site.register(Success_Indicator)
admin.site.register(Year)
