from django import forms
from django.forms import ModelForm

from .models import (
    Proc_Year,
)

class Proc_YearForm(forms.ModelForm):
    class Meta:
        model = Proc_Year
        fields = [
            'year',
        ]
