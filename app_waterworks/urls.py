from django.urls import path
from .import views

from .views import (
    Ntws_Home_Page,
)

urlpatterns = [
    path('', Ntws_Home_Page.as_view(), name = 'ntws_home'),
]
