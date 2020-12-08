from .serializers import Scan_AttendaceSerializer
from model_hris.dtr.models import (
    Scan_Attendace
)
from rest_framework import generics

class Scan_AttendaceViewSet(generics.CreateAPIView):
    serializer_class = Scan_AttendaceSerializer
    queryset = Scan_Attendace.objects.all()
