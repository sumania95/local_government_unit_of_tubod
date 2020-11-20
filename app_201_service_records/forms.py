from django import forms
from django.forms import ModelForm
from .models import Service_Record
class Service_RecordForm(forms.ModelForm):
    class Meta:
        model = Service_Record
        fields = [
            'date_from',
            'date_to',
            'designate',
            'status',
            'salary',
            'station',
            'branch',
            'lwabs',
            'separtion_date',
        ]
    # def __init__(self, *args, **kwargs):
    #     super(Service_RecordForm, self).__init__(*args, **kwargs)
    #     self.fields['designate'].widget.attrs={
    #         'class': 'form-control-sm',}
    #     self.fields['status'].widget.attrs={
    #         'class': 'form-control-sm',}
    #     self.fields['salary'].widget.attrs={
    #         'class': 'form-control-sm',}
    #     self.fields['station'].widget.attrs={
    #         'class': 'form-control-sm',}
    #     self.fields['branch'].widget.attrs={
    #         'class': 'form-control-sm',}
    #     self.fields['lwabs'].widget.attrs={
    #         'class': 'form-control-sm',}
    #     self.fields['separtion_date'].widget.attrs={
    #         'class': 'form-control-sm',}
    #     self.fields['date_from'].widget.attrs={
    #         'class': 'form-control-sm',}
    #     self.fields['date_to'].widget.attrs={
    #         'class': 'form-control-sm',}
