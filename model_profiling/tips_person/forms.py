from django import forms
from django.forms import ModelForm
from .models import Person

gender = (
    ('1', 'Male',),
    ('2', 'Female',),
)

civil_status = (
    ('1', 'Single',),
    ('2', 'Married',),
    ('3', 'Widowed',),
    ('4', 'Separated',),
    ('5', 'Annulled',),
)

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
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
            'relationship',
            'highest_educational_attainment',
            'skills',
            'occupation',
            'income',
        ]
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['firstname'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['middlename'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['surname'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['ext_name'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['date_of_birth'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['place_of_birth'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['sex'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['civil_status'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['philhealth'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['religion'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['nationality'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['relationship'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['highest_educational_attainment'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['skills'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['occupation'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['income'].widget.attrs={
            'class': 'form-control-sm',}
