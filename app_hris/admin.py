from django.contrib import admin
from .models import (
    Administrator,
    Settings
)

admin.site.register(Administrator)
admin.site.register(Settings)
