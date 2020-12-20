from django import forms
from django.forms import ModelForm
from .models import (
    Tips_Farmer,
    Tips_Farmerworker,
    Tips_Fisherfolk,
)

class Tips_FarmerForm(forms.ModelForm):
    class Meta:
        model = Tips_Farmer
        fields = [
            'is_rice',
            'is_corn',
            'other_crops',
            'livestock',
            'poultry',
        ]
