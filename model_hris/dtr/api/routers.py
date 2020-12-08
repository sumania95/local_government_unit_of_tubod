from rest_framework.routers import DefaultRouter
from .views import Scan_AttendaceViewSet

router = DefaultRouter()
router.register('scan_attendance', Scan_AttendaceViewSet, basename='scan_attendance_create')
