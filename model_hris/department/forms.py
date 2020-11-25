from django import forms
from django.forms import ModelForm
from model_hris.department.models import (
    Department,
)

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = [
            'name',
        ]
