from django.db import models
from django.db.models import Model, ForeignKey, ManyToManyField
from app_info_profile.models import Profile
from django.utils import timezone

type = (
    ('Managerial', 'Managerial',),
    ('Supervisory', 'Supervisory',),
    ('Technical', 'Technical',),
)

class Learning_Development(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200,blank=True)
    fromdate = models.DateField()
    todate = models.DateField()
    nohrs = models.IntegerField(default=0)
    typeofld = models.CharField(max_length=100,choices=type)
    sponsoredby = models.CharField(max_length = 200,blank=True)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    now = timezone.now()

    @property
    def age(self):
        return int((now.date() - self.fromdate).days / 365.25)

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
    date_of_birth = models.DateField()
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
    ('1', 'Managerial',),
    ('2', 'Supervisory',),
    ('3', 'Technical',),
)

class Educational_Background(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    level = models.CharField(max_length=100,choices=level_education)
    school_name = models.CharField(max_length = 200,blank=True)
    course = models.CharField(max_length = 200,blank=True)
    period_from = models.IntegerField(default=0)
    period_to = models.IntegerField(default=0)
    units_earned = models.IntegerField(default=0)
    year_graduated = models.IntegerField(default=0)
    academic_received = models.CharField(max_length = 200,blank=True)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

class Eligibility(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    career_service = models.CharField(max_length = 200)
    rating = models.DecimalField(default=0,max_digits = 50,decimal_places=2)
    date_of_examination = models.DateField(null=True,blank=True)
    place_of_examination = models.CharField(max_length = 200,blank=True)
    examinee_number = models.IntegerField(default=0)
    date_of_validity = models.DateField(null=True,blank=True)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

class Other_Information(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    is_question1 = models.BooleanField(default=False)
    label1 = models.CharField(max_length = 30,blank=True)
    is_question2 = models.BooleanField(default=False)
    label2 = models.CharField(max_length = 30,blank=True)
    is_question3 = models.BooleanField(default=False)
    label3 = models.CharField(max_length = 30,blank=True)
    is_question4 = models.BooleanField(default=False)
    label4 = models.CharField(max_length = 30,blank=True)
    is_question5 = models.BooleanField(default=False)
    label5 = models.CharField(max_length = 30,blank=True)
    is_question6 = models.BooleanField(default=False)
    label6 = models.CharField(max_length = 30,blank=True)
    is_question7 = models.BooleanField(default=False)
    label7 = models.CharField(max_length = 30,blank=True)
    is_question8 = models.BooleanField(default=False)
    label8 = models.CharField(max_length = 30,blank=True)
    is_question9 = models.BooleanField(default=False)
    label9 = models.CharField(max_length = 30,blank=True)
    is_question9 = models.BooleanField(default=False)
    label9 = models.CharField(max_length = 30,blank=True)
    is_question10 = models.BooleanField(default=False)
    label10 = models.CharField(max_length = 30,blank=True)
    is_question11 = models.BooleanField(default=False)
    label11 = models.CharField(max_length = 30,blank=True)
    is_question12 = models.BooleanField(default=False)
    label12 = models.CharField(max_length = 30,blank=True)

class Reference(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    referencesname1 = models.CharField(max_length = 200,blank=True)
    referencesaddress1 = models.CharField(max_length = 200,blank=True)
    referencestel1 = models.CharField(max_length = 200,blank=True)
    referencesname2 = models.CharField(max_length = 200,blank=True)
    referencesaddress2 = models.CharField(max_length = 200,blank=True)
    referencestel2 = models.CharField(max_length = 200,blank=True)
    referencesname3 = models.CharField(max_length = 200,blank=True)
    referencesaddress3 = models.CharField(max_length = 200,blank=True)
    referencestel3 = models.CharField(max_length = 200,blank=True)
