from django import forms
from django.forms import ModelForm
from .models import (
    Tips_Person,
    Tips_Address
)
from model_profiling.tips_address.models import (
    Tips_Region,
    Tips_Province,
    Tips_City_Municipality,
    Tips_Barangay,
)

class Tips_Update_AddressForm(forms.ModelForm):
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
        region = self.initial['region']
        province = self.initial['province']
        city_municipality = self.initial['city_municipality']
        barangay = self.initial['barangay']
        print(city_municipality)
        self.fields['province'].queryset = Tips_Province.objects.filter(region_id = region)
        self.fields['city_municipality'].queryset = Tips_City_Municipality.objects.filter(province_id=province)
        self.fields['barangay'].queryset = Tips_Barangay.objects.filter(city_municipality_id=city_municipality)
        if 'region' in self.data:
            try:
                id = int(self.data.get('region'))
                region = Tips_Region.objects.get(id=id)
                self.fields['province'].queryset = Tips_Province.objects.filter(region_id=region.id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset

        if 'province' in self.data:
            try:
                id = int(self.data.get('province'))
                province = Tips_Province.objects.get(id=id)
                self.fields['city_municipality'].queryset = Tips_City_Municipality.objects.filter(province_id=province.id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset

        if 'city_municipality' in self.data:
            try:
                id = int(self.data.get('city_municipality'))
                city_municipality = Tips_City_Municipality.objects.get(id=id)
                self.fields['barangay'].queryset = Tips_Barangay.objects.filter(city_municipality_id=city_municipality.id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset

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

        if 'region' in self.data:
            try:
                id = int(self.data.get('region'))
                region = Tips_Region.objects.get(id=id)
                self.fields['province'].queryset = Tips_Province.objects.filter(region_id=region.id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['province'].queryset = self.instance.region.province_set

        if 'province' in self.data:
            try:
                id = int(self.data.get('province'))
                province = Tips_Province.objects.get(id=id)
                self.fields['city_municipality'].queryset = Tips_City_Municipality.objects.filter(province_id=province.id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city_municipality'].queryset = self.instance.city_municipality.province_set

        if 'city_municipality' in self.data:
            try:
                id = int(self.data.get('city_municipality'))
                city_municipality = Tips_City_Municipality.objects.get(id=id)
                self.fields['barangay'].queryset = Tips_Barangay.objects.filter(city_municipality_id=city_municipality.id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['barangay'].queryset = self.instance.barangay.city_municipality_set

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
