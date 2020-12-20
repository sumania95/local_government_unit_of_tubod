from django.contrib import admin

from .models import (
    Tips_Recommended_Services,
    Tips_Recommended_Services_Action,
    Tips_Category,
    Tips_Sub_Category,
)

admin.site.register(Tips_Recommended_Services)
admin.site.register(Tips_Recommended_Services_Action)
admin.site.register(Tips_Category)
admin.site.register(Tips_Sub_Category)
