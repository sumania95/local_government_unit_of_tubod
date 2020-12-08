from django.urls import path,include
from .import views
from .routers import router
from .views import (
    Scan_AttendaceViewSet,
)
urlpatterns = [
    path('attendance/create', Scan_AttendaceViewSet.as_view()),
]
