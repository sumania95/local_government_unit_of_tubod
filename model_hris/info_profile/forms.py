from django import forms
from django.forms import ModelForm

from model_hris.info_profile.models import Profile

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not Profile.objects.filter(user__username = user.username):
            raise forms.ValidationError('Please enter a correct username and password. Note that both fields may be case-sensitive.', code='invalid_login')
        if Profile.objects.filter(user__username = user.username, is_active = False):
            raise forms.ValidationError('Your Account has been deactivate. Contact Your Administrator', code='invalid_login')

class UsernameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username'
            ]

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

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'firstname',
            'middlename',
            'surname',
            'ext_name',
            'date_of_birth',
            'place_of_birth',
            'sex',
            'civil_status',
            'height',
            'weight',
            'blood_type',
            'gsis',
            'pagibig',
            'philhealth',
            'sss',
            'tin',
            'agency_no',
            'citizenship',
            'residential_address',
            'zipcode_1',
            'permanent_address',
            'zipcode_2',
            'telephone',
            'mobile',
            'email',
            'image',
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
        self.fields['height'].widget.attrs={
            'class': 'form-control-sm',}

        self.fields['weight'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['blood_type'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['gsis'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['pagibig'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['philhealth'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['sss'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['tin'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['agency_no'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['citizenship'].widget.attrs={
            'class': 'form-control-sm',}

        self.fields['residential_address'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['zipcode_1'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['permanent_address'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['zipcode_2'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['telephone'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['mobile'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['email'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['image'].widget.attrs={
            'class': 'form-control-sm',}
