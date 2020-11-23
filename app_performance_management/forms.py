from django import forms
from django.forms import ModelForm

from .models import (
    Accomplishment,
    # Actual_Accomplishment,
    Success_Indicator,
    Year,
    Rating_Accomplishment,
)

class AccomplishmentForm(forms.ModelForm):
    class Meta:
        model = Accomplishment
        fields = [
            'core_function_output',
        ]

# class Actual_AccomplishmentForm(forms.ModelForm):
#     actual_accomplishment = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,'style' : "white-space: pre-wrap"},),)
#     class Meta:
#         model = Actual_Accomplishment
#         fields = [
#             'actual_accomplishment',
#         ]

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

class Rating_AccomplishmentForm(forms.ModelForm):
    class Meta:
        model = Rating_Accomplishment
        fields = [
            'actual_accomplishment',
            'ratings',
            'remarks',
        ]
