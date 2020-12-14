from django.urls import path
from .import views

from .views import (
    Ntws_Dashboard_Page,
)

urlpatterns = [
    path('', Ntws_Dashboard_Page.as_view(), name = 'ntws_home'),
]
