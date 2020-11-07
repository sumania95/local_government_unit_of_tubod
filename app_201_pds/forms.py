from django import forms
from django.forms import ModelForm

from .models import (
    Family_Background,
    Children,
    Educational_Background,
    Eligibility,
    Work_Experience,
    Voluntary_Work,
    Learning_Development,
    Q34,
    Q35,
    Q36,
    Q37,
    Q38,
    Q39,
    Q40,
    References1,
    References2,
    References3,
    Government_Other_Info,

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

class Voluntary_WorkForm(forms.ModelForm):
    class Meta:
        model = Voluntary_Work
        fields = [
            'date_from',
            'date_to',
            'organization',
            'no_hrs',
            'nature_of_work',
        ]

class Learning_DevelopmentForm(forms.ModelForm):
    class Meta:
        model = Learning_Development
        fields = [
            'date_from',
            'date_to',
            'title',
            'no_hrs',
            'type_of_ld',
            'sponsored_by',
        ]

class Q34Form(forms.ModelForm):
    class Meta:
        model = Q34
        fields = [
            'question_1',
            'detail_1',
            'question_2',
            'detail_2',
        ]

class Q35Form(forms.ModelForm):
    class Meta:
        model = Q35
        fields = [
            'question_1',
            'detail_1',
            'question_2',
            'detail_2',
        ]

class Q36Form(forms.ModelForm):
    class Meta:
        model = Q36
        fields = [
            'question_1',
            'detail_1',
        ]

class Q37Form(forms.ModelForm):
    class Meta:
        model = Q37
        fields = [
            'question_1',
            'detail_1',
        ]

class Q38Form(forms.ModelForm):
    class Meta:
        model = Q38
        fields = [
            'question_1',
            'detail_1',
            'question_2',
            'detail_2',
        ]

class Q39Form(forms.ModelForm):
    class Meta:
        model = Q39
        fields = [
            'question_1',
            'detail_1',
        ]

class Q40Form(forms.ModelForm):
    class Meta:
        model = Q40
        fields = [
            'question_1',
            'detail_1',
            'question_2',
            'detail_2',
            'question_3',
            'detail_3',
            'question_4',
            'detail_4',
        ]

class References1Form(forms.ModelForm):
    class Meta:
        model = References1
        fields = [
            'name',
            'address',
            'tel_no',
        ]

class References2Form(forms.ModelForm):
    class Meta:
        model = References2
        fields = [
            'name',
            'address',
            'tel_no',
        ]


class References3Form(forms.ModelForm):
    class Meta:
        model = References3
        fields = [
            'name',
            'address',
            'tel_no',
        ]

class Government_Other_InfoForm(forms.ModelForm):
    class Meta:
        model = Government_Other_Info
        fields = [
            'issued_id',
            'id_no',
            'date_issued',
        ]
