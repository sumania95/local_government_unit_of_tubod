from django import forms
from django.forms import ModelForm
from model_hris.internet.models import (
    Voucher,
    Generate_Ticket,
)

class VoucherForm(forms.ModelForm):
    class Meta:
        model = Voucher
        fields = [
            'voucher',
        ]

class Generate_TicketForm(forms.ModelForm):
    class Meta:
        model = Generate_Ticket
        fields = [
            'no_ticket',
        ]
