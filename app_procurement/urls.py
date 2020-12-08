from django.urls import path
from .import views

from .views import (
    Proc_Home_Page,
)

urlpatterns = [
    path('', Proc_Home_Page.as_view(), name = 'proc_home'),
]
