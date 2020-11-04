from django import forms
from django.forms import ModelForm

from .models import (
    Family_Background,
    Children,
    Educational_Background,
    Eligibility,
    Work_Experience,
    Voluntary_Work,
)

class Family_BackgroundForm(forms.ModelForm):
    class Meta:
        model = Family_Background
        fields = [
            'spousesurname',
            'spousefirstname',
            'spousemiddlename',
            'spouseextname',
            'spouseoccupation',
            'spouseemployer',
            'spouseemployeraddress',
            'spousetelephone',
            'spouse_government_issued_id',
            'spouse_government_id_no',
            'spouse_government_date_issued',
            'fathersurname',
            'fatherfirstname',
            'fathermiddlename',
            'fatherextname',
            'mothersurname',
            'motherfirstname',
            'mothermiddlename',
        ]

class ChildrenForm(forms.ModelForm):
    class Meta:
        model = Children
        fields = [
            'surname',
            'firstname',
            'middlename',
            'extname',
            'date_of_birth',
            'civil_status',
        ]

class Educational_BackgroundForm(forms.ModelForm):
    class Meta:
        model = Educational_Background
        fields = [
            'level',
            'school_name',
            'course',
            'period_from',
            'period_to',
            'units_earned',
            'year_graduated',
            'academic_received',
        ]

class EligibilityForm(forms.ModelForm):
    class Meta:
        model = Eligibility
        fields = [
            'career_service',
            'rating',
            'date_of_examination',
            'place_of_examination',
            'examinee_number',
            'date_of_validity',
        ]

class Work_ExperienceForm(forms.ModelForm):
    class Meta:
        model = Work_Experience
        fields = [
            'date_from',
            'date_to',
            'position_title',
            'department_office',
            'salary',
            'pay_grade',
            'status',
            'is_governtment_service',
        ]
