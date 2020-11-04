from django import forms
from django.forms import ModelForm

from .models import (
    Settings,
)

class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = [
            'name',
            'address',
            'dtr_from',
            'dtr_to',
        ]
