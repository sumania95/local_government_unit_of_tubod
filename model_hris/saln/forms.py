from django import forms
from django.forms import ModelForm
from model_hris.saln.models import (
    Business_Interest_Financial_Connections,
    Liabilities,
    Personal_Properties,
    Real_Properties,
    Relatives_In_The_Government_Service,
)

class Relatives_In_The_Government_ServiceForm(forms.ModelForm):
    description = forms.CharField(label="")
    class Meta:
        model = Relatives_In_The_Government_Service
        fields = [
            'description',
        ]
