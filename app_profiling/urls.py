from django.urls import path
from .import views

from .views import (
    Profiling_Dashboard_Page,
)

urlpatterns = [
    path('', Profiling_Dashboard_Page.as_view(), name = 'profiling_home'),
]
