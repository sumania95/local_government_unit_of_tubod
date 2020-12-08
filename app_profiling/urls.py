from django.urls import path
from .import views

from .views import (
    Tips_Dashboard_Page,
    Tips_Person_Page
)

urlpatterns = [
    path('', Tips_Dashboard_Page.as_view(), name = 'tips_home'),
    path('person', Tips_Person_Page.as_view(), name = 'tips_person'),
]
