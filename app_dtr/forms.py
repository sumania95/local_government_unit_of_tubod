from django import forms
from django.forms import ModelForm

from .models import (
    Dtr_Assign
)

class Dtr_AssignForm(forms.ModelForm):
    class Meta:
        model = Dtr_Assign
        fields = [
            'profile',
            'id',
        ]
