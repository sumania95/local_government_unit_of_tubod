from django import forms
from django.forms import ModelForm
from model_hris.designation.models import (
    Plantilla,
    Designation,
    Contractual,
)
from model_hris.info_profile.models import (
    Profile,
)
class PlantillaForm(forms.ModelForm):
    class Meta:
        model = Plantilla
        fields = [
            'item_no',
            'department',
            'organizationalunit',
            'positiontitle',
            'salarygrade',
            'authorizedannualsalary',
            'actualannualsalary',
            'areacode',
            'areatype',
            'level',
            'status',
            'is_available',
        ]

class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = [
            'profile',
            'date_appointed',
        ]
    def __init__(self, *args, **kwargs):
        super(DesignationForm, self).__init__(*args, **kwargs)
        queryset01=Profile.objects.exclude(id__in = Designation.objects.values('profile_id'))
        self.fields['profile']=forms.ModelChoiceField(queryset = queryset01.exclude(id__in = Contractual.objects.values('profile_id')).order_by('surname','firstname'))

class ContractualUpdateForm(forms.ModelForm):
    class Meta:
        model = Contractual
        fields = [
            'positiontitle',
            'status',
            'basic_salary',
            'department',
            'date_appointed',
        ]


class ContractualForm(forms.ModelForm):
    class Meta:
        model = Contractual
        fields = [
            'profile',
            'positiontitle',
            'status',
            'basic_salary',
            'department',
            'date_appointed',
        ]
    def __init__(self, *args, **kwargs):
        super(ContractualForm, self).__init__(*args, **kwargs)
        queryset01=Profile.objects.exclude(id__in = Designation.objects.values('profile_id'))
        self.fields['profile']=forms.ModelChoiceField(queryset = queryset01.exclude(id__in = Contractual.objects.values('profile_id')).order_by('surname','firstname'))
