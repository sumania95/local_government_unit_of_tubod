from django import forms
from django.forms import ModelForm

from .models import (
    Accomplishment,
)

class AccomplishmentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            'core_function_output',
        ]
