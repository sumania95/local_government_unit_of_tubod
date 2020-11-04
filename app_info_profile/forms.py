from django import forms
from django.forms import ModelForm

from .models import Profile

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not Profile.objects.filter(user__username = user.username):
            raise forms.ValidationError('Please enter a correct username and password. Note that both fields may be case-sensitive.', code='invalid_login')
        if Profile.objects.filter(user__username = user.username, is_active = False):
            raise forms.ValidationError('Your Account has been deactivate. Contact Your Administrator', code='invalid_login')

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
        ]
