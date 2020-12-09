from django import forms
from django.forms import ModelForm

from model_hris.pds.models import (
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
    def __init__(self, *args, **kwargs):
        super(Family_BackgroundForm, self).__init__(*args, **kwargs)
        self.fields['spousesurname'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['spousefirstname'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['spousemiddlename'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['spouseextname'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['spouseoccupation'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['spouseemployer'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['spouseemployeraddress'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['spousetelephone'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['spouse_government_issued_id'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['spouse_government_id_no'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['spouse_government_date_issued'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['fathersurname'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['fatherfirstname'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['fathermiddlename'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['fatherextname'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['mothersurname'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['motherfirstname'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['mothermiddlename'].widget.attrs={
            'class': 'form-control-sm',}



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
    def __init__(self, *args, **kwargs):
        super(ChildrenForm, self).__init__(*args, **kwargs)
        self.fields['surname'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['firstname'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['middlename'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['extname'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['date_of_birth'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['civil_status'].widget.attrs={
            'class': 'form-control-sm',}

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
    def __init__(self, *args, **kwargs):
        super(Educational_BackgroundForm, self).__init__(*args, **kwargs)
        self.fields['level'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['school_name'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['course'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['period_from'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['period_to'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['units_earned'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['year_graduated'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['academic_received'].widget.attrs={
            'class': 'form-control-sm',}

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
    def __init__(self, *args, **kwargs):
        super(EligibilityForm, self).__init__(*args, **kwargs)
        self.fields['career_service'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['date_of_examination'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['place_of_examination'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['examinee_number'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['date_of_validity'].widget.attrs={
            'class': 'form-control-sm',}

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
    def __init__(self, *args, **kwargs):
        super(Work_ExperienceForm, self).__init__(*args, **kwargs)
        self.fields['date_from'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['date_to'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['position_title'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['department_office'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['pay_grade'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['status'].widget.attrs={
            'class': 'form-control-sm',}

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
    def __init__(self, *args, **kwargs):
        super(Voluntary_WorkForm, self).__init__(*args, **kwargs)
        self.fields['date_from'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['date_to'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['organization'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['no_hrs'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['nature_of_work'].widget.attrs={
            'class': 'form-control-sm',}

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
    def __init__(self, *args, **kwargs):
        super(Learning_DevelopmentForm, self).__init__(*args, **kwargs)
        self.fields['date_from'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['date_to'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['title'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['no_hrs'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['type_of_ld'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['sponsored_by'].widget.attrs={
            'class': 'form-control-sm',}

class Q34Form(forms.ModelForm):
    class Meta:
        model = Q34
        fields = [
            'question_1',
            'detail_1',
            'question_2',
            'detail_2',
        ]
    def __init__(self, *args, **kwargs):
        super(Q34Form, self).__init__(*args, **kwargs)
        self.fields['detail_1'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['detail_2'].widget.attrs={
            'class': 'form-control-sm',}

class Q35Form(forms.ModelForm):
    class Meta:
        model = Q35
        fields = [
            'question_1',
            'detail_1',
            'question_2',
            'detail_2',
        ]
    def __init__(self, *args, **kwargs):
        super(Q35Form, self).__init__(*args, **kwargs)
        self.fields['detail_1'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['detail_2'].widget.attrs={
            'class': 'form-control-sm',}

class Q36Form(forms.ModelForm):
    class Meta:
        model = Q36
        fields = [
            'question_1',
            'detail_1',
        ]
    def __init__(self, *args, **kwargs):
        super(Q36Form, self).__init__(*args, **kwargs)
        self.fields['detail_1'].widget.attrs={
            'class': 'form-control-sm',}

class Q37Form(forms.ModelForm):
    class Meta:
        model = Q37
        fields = [
            'question_1',
            'detail_1',
        ]
    def __init__(self, *args, **kwargs):
        super(Q37Form, self).__init__(*args, **kwargs)
        self.fields['detail_1'].widget.attrs={
            'class': 'form-control-sm',}

class Q38Form(forms.ModelForm):
    class Meta:
        model = Q38
        fields = [
            'question_1',
            'detail_1',
            'question_2',
            'detail_2',
        ]
    def __init__(self, *args, **kwargs):
        super(Q38Form, self).__init__(*args, **kwargs)
        self.fields['detail_1'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['detail_2'].widget.attrs={
            'class': 'form-control-sm',}

class Q39Form(forms.ModelForm):
    class Meta:
        model = Q39
        fields = [
            'question_1',
            'detail_1',
        ]
    def __init__(self, *args, **kwargs):
        super(Q39Form, self).__init__(*args, **kwargs)
        self.fields['detail_1'].widget.attrs={
            'class': 'form-control-sm',}

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
    def __init__(self, *args, **kwargs):
        super(Q40Form, self).__init__(*args, **kwargs)
        self.fields['detail_1'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['detail_2'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['detail_3'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['detail_4'].widget.attrs={
            'class': 'form-control-sm',}

class References1Form(forms.ModelForm):
    class Meta:
        model = References1
        fields = [
            'name',
            'address',
            'tel_no',
        ]
    def __init__(self, *args, **kwargs):
        super(References1Form, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['address'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['tel_no'].widget.attrs={
            'class': 'form-control-sm',}

class References2Form(forms.ModelForm):
    class Meta:
        model = References2
        fields = [
            'name',
            'address',
            'tel_no',
        ]
    def __init__(self, *args, **kwargs):
        super(References2Form, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['address'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['tel_no'].widget.attrs={
            'class': 'form-control-sm',}


class References3Form(forms.ModelForm):
    class Meta:
        model = References3
        fields = [
            'name',
            'address',
            'tel_no',
        ]
    def __init__(self, *args, **kwargs):
        super(References3Form, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['address'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['tel_no'].widget.attrs={
            'class': 'form-control-sm',}

class Government_Other_InfoForm(forms.ModelForm):
    class Meta:
        model = Government_Other_Info
        fields = [
            'issued_id',
            'id_no',
            'date_issued',
        ]
    def __init__(self, *args, **kwargs):
        super(Government_Other_InfoForm, self).__init__(*args, **kwargs)
        self.fields['issued_id'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['id_no'].widget.attrs={
            'class': 'form-control-sm',}
        self.fields['date_issued'].widget.attrs={
            'class': 'form-control-sm',}
