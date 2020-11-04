from django import forms
from django.forms import ModelForm
from .models import Service_Record
class Service_RecordForm(forms.ModelForm):
    class Meta:
        model = Service_Record
        fields = [
            'designate',
            'status',
            'salary',
            'station',
            'branch',
            'lwabs',
            'separtion_date',
            'date_from',
            'date_to',
        ]
