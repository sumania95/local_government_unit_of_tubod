from django import forms
from django.forms import ModelForm
from .models import (
    Tips_Land_Description,
    Tips_Livestock_Poultry,
)
from model_profiling.tips_address.models import (
    Tips_Barangay,
)

class Tips_Land_DescriptionForm(forms.ModelForm):
    class Meta:
        model = Tips_Land_Description
        fields = [
            'barangay',
            'ownership_document',
            'size',
            'status',
            'specify',
            'commodity',
            'farm_type',
            'is_organic',
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['barangay'].queryset = Tips_Barangay.objects.filter(city_municipality_id = 166727)

class Tips_Livestock_PoultryForm(forms.ModelForm):
    class Meta:
        model = Tips_Livestock_Poultry
        fields = [
            'specify',
            'no_of_heads',
        ]
