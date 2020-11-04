from django import forms
from django.forms import ModelForm
from .models import Voucher
class VoucherForm(forms.ModelForm):
    class Meta:
        model = Voucher
        fields = [
            'reason',
        ]
