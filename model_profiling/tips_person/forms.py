from django import forms
from django.forms import ModelForm
from .models import (
    Tips_Person,
    Tips_Address
)
from model_profiling.tips_address.models import (
    Tips_Province,
    Tips_City_Municipality,
    Tips_Barangay,
)
class Tips_AddressForm(forms.ModelForm):
    class Meta:
        model = Tips_Address
        fields = [
            'region',
            'province',
            'city_municipality',
            'barangay',
            'purok_street',
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['province'].queryset = Tips_Province.objects.none()
        self.fields['city_municipality'].queryset = Tips_City_Municipality.objects.none()
        self.fields['barangay'].queryset = Tips_Barangay.objects.none()

class Tips_PersonForm(forms.ModelForm):
    class Meta:
        model = Tips_Person
        fields = [
            'firstname',
            'middlename',
            'surname',
            'ext_name',
            'date_of_birth',
            'place_of_birth',
            'sex',
            'civil_status',
            'philhealth',
            'religion',
            'nationality',
            'highest_educational_attainment',
            'skills_occupation',
            'income',
        ]
    # def __init__(self, *args, **kwargs):
    #     super(Tips_PersonForm, self).__init__(*args, **kwargs)
    #     self.fields['firstname'].widget.attrs={
    #         'class': 'form-control-sm',}
    #     self.fields['middlename'].widget.attrs={
    #         'class': 'form-control-sm',}
    #     self.fields['surname'].widget.attrs={
    #         'class': 'form-control-sm',}
    #     self.fields['ext_name'].widget.attrs={
    #         'class': 'form-control-sm',}
    #     self.fields['date_of_birth'].widget.attrs={
    #         'class': 'form-control-sm',}
    #     self.fields['place_of_birth'].widget.attrs={
    #         'class': 'form-control-sm',}
    #     self.fields['sex'].widget.attrs={
    #         'class': 'form-control-sm',}
    #     self.fields['civil_status'].widget.attrs={
    #         'class': 'form-control-sm',}
    #     self.fields['philhealth'].widget.attrs={
    #         'class': 'form-control-sm',}
    #     self.fields['religion'].widget.attrs={
    #         'class': 'form-control-sm',}
    #     self.fields['nationality'].widget.attrs={
    #         'class': 'form-control-sm',}
    #     self.fields['highest_educational_attainment'].widget.attrs={
    #         'class': 'form-control-sm',}
    #     self.fields['skills_occupation'].widget.attrs={
    #         'class': 'form-control-sm',}
    #     self.fields['income'].widget.attrs={
    #         'class': 'form-control-sm',}
