from django.contrib import admin

from .models import (
    Rating,
    Accomplishment,
    Success_Indicator,
    Year,
)


admin.site.register(Rating)
admin.site.register(Accomplishment)
admin.site.register(Success_Indicator)
admin.site.register(Year)
