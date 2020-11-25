from django import forms
from django.forms import ModelForm

from model_hris.dtr.models import (
    Dtr_Assign
)

class Dtr_AssignForm(forms.ModelForm):
    class Meta:
        model = Dtr_Assign
        fields = [
            'profile',
            'id',
        ]
