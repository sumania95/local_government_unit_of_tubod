from django import forms
from django.forms import ModelForm

from .models import Rewards_Recognitions
from app_info_profile.models import Profile
class Rewards_RecognitionsForm(forms.ModelForm):
    class Meta:
        model = Rewards_Recognitions
        fields = [
            'profile',
            'title',
            'sponsored',
        ]
