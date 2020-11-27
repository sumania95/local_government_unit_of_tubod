from django import forms
from django.forms import ModelForm
from model_hris.document.models import (
    Document,
)

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = [
            'name',
            'file',
        ]
