from django import forms
from django.forms import ModelForm
from model_hris.saln.models import (
    Saln_Business_Interest_Financial_Connections,
    Saln_Liabilities,
    Saln_Personal_Properties,
    Saln_Real_Properties,
    Saln_Relatives_In_The_Government_Service,
    Saln_Filling,
)

class Saln_FillingForm(forms.ModelForm):
    class Meta:
        model = Saln_Filling
        fields = [
            'filling_type',
        ]

class Saln_Business_Interest_Financial_ConnectionsForm(forms.ModelForm):
    class Meta:
        model = Saln_Business_Interest_Financial_Connections
        fields = [
            'business_enterprise',
            'business_address',
            'nature_of_business',
            'date_of_acquisition_of_interest',
        ]
    def __init__(self, *args, **kwargs):
        super(Saln_Business_Interest_Financial_ConnectionsForm, self).__init__(*args, **kwargs)
        self.fields['business_enterprise'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['business_address'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['nature_of_business'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['date_of_acquisition_of_interest'].widget.attrs={
            'class': 'form-control-sm',}

class Saln_LiabilitiesForm(forms.ModelForm):
    class Meta:
        model = Saln_Liabilities
        fields = [
            'nature',
            'name_of_creditors',
            'outstanding_balance',
        ]

class Saln_Personal_PropertiesForm(forms.ModelForm):
    class Meta:
        model = Saln_Personal_Properties
        fields = [
            'description',
            'year',
            'acquisition_cost',
        ]

class Saln_Real_PropertiesForm(forms.ModelForm):
    class Meta:
        model = Saln_Real_Properties
        fields = [
            'description',
            'kind',
            'exact_location',
            'assessed_value',
            'current_fair_market_value',
            'year',
            'mode',
            'acquisition_cost',
        ]

class Saln_Relatives_In_The_Government_ServiceForm(forms.ModelForm):
    class Meta:
        model = Saln_Relatives_In_The_Government_Service
        fields = [
            'name_of_relative',
            'relationship',
            'position',
            'name_of_agency',
        ]
