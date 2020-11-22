from django import forms
from django.forms import ModelForm
from .models import (
    Department,
)

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = [
            'name',
        ]
