from django import forms
from django.forms import ModelForm
from .models import (
    Tips_Recommended_Services,
    Tips_Recommended_Services_Action,
    Tips_Category,
    Tips_Sub_Category
)

class Tips_Recommended_ServicesForm(forms.ModelForm):
    class Meta:
        model = Tips_Recommended_Services
        fields = [
            'services_assistance',
            'specify',
        ]

class Tips_Recommended_Services_ActionForm(forms.ModelForm):
    class Meta:
        model = Tips_Recommended_Services_Action
        fields = [
            'category',
            'sub_category',
            'amount',
            'mode_assistance',
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sub_category'].queryset = Tips_Sub_Category.objects.none()

        if 'category' in self.data:
            try:
                id = int(self.data.get('category'))
                category = Tips_Sub_Category.objects.get(id=id)
                self.fields['sub_category'].queryset = Tips_Sub_Category.objects.filter(category_id=category.id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['sub_category'].queryset = self.instance.category.sub_category_set

class Tips_Recommended_Services_Action_UpdateForm(forms.ModelForm):
    class Meta:
        model = Tips_Recommended_Services_Action
        fields = [
            'category',
            'sub_category',
            'amount',
            'mode_assistance',
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        category = self.initial['category']
        sub_category = self.initial['sub_category']
        self.fields['sub_category'].queryset = Tips_Sub_Category.objects.filter(category_id = category)
        if 'category' in self.data:
            try:
                id = int(self.data.get('category'))
                category = Tips_Sub_Category.objects.get(id=id)
                self.fields['sub_category'].queryset = Tips_Sub_Category.objects.filter(category_id=category.id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
