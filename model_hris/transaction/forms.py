from django import forms
from django.forms import ModelForm

from model_hris.transaction.models import (
    Deducted_Transaction,
    Deducted_Action_Transaction,
    Generated_Transaction,
    Batch_Generated_Transaction,
    Rejected_Transaction,
)
from model_hris.info_profile.models import Profile

leave_type = (
    ('1', 'Sick Leave',),
    ('2', 'Vacation Leave',),
    ('4', 'Offset',),
)

leave_type_contractual = (
    ('4', 'Offset',),
)

class Deducted_TransactionForm(forms.ModelForm):
    class Meta:
        model = Deducted_Transaction
        fields = [
            'leave_type',
            'profile',
            'description',
            'date_from',
            'date_to',
        ]
class User_Deducted_Contractual_TransactionForm(forms.ModelForm):
    leave_type = forms.ChoiceField(choices=leave_type_contractual)
    class Meta:
        model = Deducted_Transaction
        fields = [
            'description',
            'leave_type',
            'date_from',
            'date_to',
        ]

class User_Deducted_TransactionForm(forms.ModelForm):
    class Meta:
        model = Deducted_Transaction
        fields = [
            'description',
            'leave_type',
            'date_from',
            'date_to',
        ]

class Deducted_Action_TransactionForm(forms.ModelForm):
    class Meta:
        model = Deducted_Action_Transaction
        fields = [
            'days',
            'remarks',
        ]
    def clean(self,*args,**kwargs):
        days = self.cleaned_data.get('days')
        if days == 0:
            raise forms.ValidationError('Warning: Zero is not allowed.')
        return super().clean()

class Rejected_TransactionForm(forms.ModelForm):
    class Meta:
        model = Rejected_Transaction
        fields = [
            'remarks',
        ]



class Generated_TransactionForm(forms.ModelForm):
    leave_type = forms.ChoiceField(choices=leave_type)
    class Meta:
        model = Generated_Transaction
        fields = [
            'leave_type',
            'profile',
            'days',
            'remarks',
        ]

class Batch_Generated_TransactionForm(forms.ModelForm):
    class Meta:
        model = Batch_Generated_Transaction
        fields = [
            'remarks',
        ]
