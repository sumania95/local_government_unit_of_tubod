from django.contrib import admin

from .models import (
    Tips_Person,
    Tips_Person_Category,
    Tips_City_Municipality,
    Tips_Region,
)

admin.site.register(Tips_Person)
admin.site.register(Tips_Person_Category)
