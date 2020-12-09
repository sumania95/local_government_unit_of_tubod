from django.db import models
from django.db.models import Model, ForeignKey, ManyToManyField
from model_hris.info_profile.models import Profile
from django.utils import timezone

type = (
    ('Managerial', 'Managerial',),
    ('Supervisory', 'Supervisory',),
    ('Technical', 'Technical',),
)

class Learning_Development(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200,blank=True)
    date_from = models.DateField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)
    no_hrs = models.IntegerField(default=8)
    type_of_ld = models.CharField(max_length=100,choices=type)
    sponsored_by = models.CharField(max_length = 200,blank=True)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    now = timezone.now()

    @property
    def age(self):
        return int((now.date() - self.fromdate).days / 365.25)

class Skill_Hobbies(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.CharField(max_length = 200,blank=True)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)


class Member_Organization(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.CharField(max_length = 200,blank=True)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

class Non_Academic(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.CharField(max_length = 200,blank=True)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)


class References1(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    tel_no = models.CharField(max_length = 200)

class References2(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    tel_no = models.CharField(max_length = 200)

class References3(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 30)
    tel_no = models.CharField(max_length = 30)

class Government_Other_Info(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    issued_id = models.CharField(max_length = 30)
    id_no = models.CharField(max_length = 30)
    date_issued = models.CharField(max_length = 30)

class Q34(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    question_1 = models.BooleanField(default=False)
    detail_1 = models.CharField(max_length = 30,blank=True)
    question_2 = models.BooleanField(default=False)
    detail_2 = models.CharField(max_length = 30,blank=True)

class Q35(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    question_1 = models.BooleanField(default=False)
    detail_1 = models.CharField(max_length = 30,blank=True)
    question_2 = models.BooleanField(default=False)
    detail_2 = models.CharField(max_length = 30,blank=True)

class Q36(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    question_1 = models.BooleanField(default=False)
    detail_1 = models.CharField(max_length = 30,blank=True)

class Q37(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    question_1 = models.BooleanField(default=False)
    detail_1 = models.CharField(max_length = 30,blank=True)

class Q38(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    question_1 = models.BooleanField(default=False)
    detail_1 = models.CharField(max_length = 30,blank=True)
    question_2 = models.BooleanField(default=False)
    detail_2 = models.CharField(max_length = 30,blank=True)

class Q39(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    question_1 = models.BooleanField(default=False)
    detail_1 = models.CharField(max_length = 30,blank=True)

class Q40(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    question_1 = models.BooleanField(default=False)
    detail_1 = models.CharField(max_length = 30,blank=True)
    question_2 = models.BooleanField(default=False)
    detail_2 = models.CharField(max_length = 30,blank=True)
    question_3 = models.BooleanField(default=False)
    detail_3 = models.CharField(max_length = 30,blank=True)
    question_4 = models.BooleanField(default=False)
    detail_4 = models.CharField(max_length = 30,blank=True)

class Family_Background(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    spousesurname = models.CharField(max_length = 200,blank=True)
    spousefirstname = models.CharField(max_length = 200,blank=True)
    spousemiddlename = models.CharField(max_length = 200,blank=True)
    spouseextname = models.CharField(max_length = 200,blank=True)
    spouseoccupation = models.CharField(max_length = 200,blank=True)
    spouseemployer = models.CharField(max_length = 200,blank=True)
    spouseemployeraddress = models.CharField(max_length = 200,blank=True)
    spousetelephone = models.CharField(max_length = 200,blank=True)
    spouse_government_issued_id = models.CharField(max_length = 200,blank=True)
    spouse_government_id_no = models.CharField(max_length = 200,blank=True)
    spouse_government_date_issued = models.DateField(null=True,blank=True)
    fathersurname = models.CharField(max_length = 200,blank=True)
    fatherfirstname = models.CharField(max_length = 200,blank=True)
    fathermiddlename = models.CharField(max_length = 200,blank=True)
    fatherextname = models.CharField(max_length = 200,blank=True)
    mothersurname = models.CharField(max_length = 200,blank=True)
    motherfirstname = models.CharField(max_length = 200,blank=True)
    mothermiddlename = models.CharField(max_length = 200,blank=True)


civil_status = (
    ('1', 'Single',),
    ('2', 'Married',),
    ('3', 'Widowed',),
    ('4', 'Separated',),
    ('5', 'Annulled',),
)

class Children(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    surname = models.CharField(max_length = 200)
    firstname = models.CharField(max_length = 200)
    middlename = models.CharField(max_length = 200,blank=True)
    extname = models.CharField(max_length = 200,blank=True)
    date_of_birth = models.DateField(default=timezone.now)
    civil_status = models.CharField(max_length=10,choices=civil_status)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    @property
    def age(self):
        now = timezone.now()
        return int((now.date() - self.date_of_birth).days / 365.25)

    def __str__(self):
        return '%s: %s' % (self.surname, self.firstname)

level_education = (
    ('1', 'Elementary',),
    ('2', 'Secondary',),
    ('3', 'Vocational / Trade Course',),
    ('4', 'College',),
    ('5', 'Graduate Studies',),
)

class Educational_Background(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    level = models.CharField(max_length=100,choices=level_education)
    school_name = models.CharField(max_length = 200,blank=True)
    course = models.CharField(max_length = 200,blank=True)
    period_from = models.IntegerField(default=timezone.now().year)
    period_to = models.IntegerField(default=timezone.now().year)
    units_earned = models.CharField(max_length = 200,blank=True)
    year_graduated = models.IntegerField(default=timezone.now().year)
    academic_received = models.CharField(max_length = 200,blank=True)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

class Eligibility(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    career_service = models.CharField(max_length = 200)
    rating = models.DecimalField(default=0,max_digits = 50,decimal_places=2)
    date_of_examination = models.CharField(max_length = 200,null=True,blank=True)
    place_of_examination = models.CharField(max_length = 200,blank=True)
    examinee_number = models.IntegerField(default=0)
    date_of_validity = models.CharField(max_length = 200,null=True,blank=True)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

class Work_Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_from = models.DateField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)
    position_title = models.CharField(max_length = 200)
    department_office = models.CharField(max_length = 200)
    salary = models.DecimalField(default= 0,max_digits = 50,decimal_places=2)
    pay_grade = models.CharField(max_length = 200)
    status = models.CharField(max_length = 200)
    is_governtment_service = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

class Voluntary_Work(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    organization = models.CharField(max_length = 200,blank=True)
    date_from = models.DateField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)
    no_hrs = models.IntegerField(default=0)
    nature_of_work = models.CharField(max_length = 200,blank=True)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)
