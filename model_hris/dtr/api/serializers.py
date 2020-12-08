from rest_framework import serializers
from django.contrib.auth.models import User
from django.db.models import Q,F,Sum,Count
from django.utils import timezone
from django.core.exceptions import ValidationError
from rest_framework import status
from model_hris.dtr.models import (
    Scan_Attendace,
)


class Scan_AttendaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scan_Attendace
        fields = [
            'profile',
        ]
