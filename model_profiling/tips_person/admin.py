from django.contrib import admin

from .models import (
    Tips_Barangay,
    Tips_Province,
    Tips_City_Municipality,
    Tips_Region,
)

admin.site.register(Tips_Barangay)
admin.site.register(Tips_Province)
admin.site.register(Tips_City_Municipality)
admin.site.register(Tips_Region)
