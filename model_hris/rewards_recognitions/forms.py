from django import forms
from django.forms import ModelForm
from model_hris.rewards_recognitions.models import Rewards_Recognitions
from model_hris.info_profile.models import Profile

class Rewards_RecognitionsForm(forms.ModelForm):
    class Meta:
        model = Rewards_Recognitions
        fields = [
            'profile',
            'title',
            'sponsored',
        ]
