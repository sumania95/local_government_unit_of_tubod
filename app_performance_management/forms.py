from django import forms
from django.forms import ModelForm

from .models import (
    Accomplishment,
    Success_Indicator,
    Year,
)

class AccomplishmentForm(forms.ModelForm):
    class Meta:
        model = Accomplishment
        fields = [
            'core_function_output',
        ]

class YearForm(forms.ModelForm):
    class Meta:
        model = Year
        fields = [
            'year',
        ]

class Success_IndicatorForm(forms.ModelForm):
    class Meta:
        model = Success_Indicator
        fields = [
            'description',
        ]
