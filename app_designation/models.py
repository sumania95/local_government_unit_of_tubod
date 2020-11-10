from django.db import models
from django.db.models import Model, ForeignKey, ManyToManyField
from app_info_profile.models import Profile
from app_department.models import Department
from django.utils import timezone

status = (
    ('1', 'Permanent',),
    ('2', 'Co-Terminus',),
    ('3', 'Elected',),
)

class Plantilla(models.Model):
    item_no = models.IntegerField(default=0)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    organizationalunit = models.CharField(max_length = 200,blank=True)
    positiontitle = models.CharField(max_length = 200)
    salarygrade = models.DecimalField(default= 0,max_digits = 50,decimal_places=0)
    authorizedannualsalary = models.DecimalField(default= 0,max_digits = 50,decimal_places=2)
    actualannualsalary = models.DecimalField(default= 0,max_digits = 50,decimal_places=2)
    areacode = models.CharField(max_length = 200)
    areatype = models.CharField(max_length = 200)
    level = models.CharField(max_length = 200)
    status = models.CharField(max_length=100,choices=status)
    is_available = models.BooleanField(default=True)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.positiontitle)

    class Meta:
        ordering = ['positiontitle']

class Designation(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    plantilla = models.OneToOneField(Plantilla, on_delete=models.CASCADE)
    date_appointed = models.DateField(default=timezone.now())
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    @property
    def stepInc(self):
        now = timezone.now()
        return int((now.date() - self.date_appointed).days / 365.25)

class Designationlog(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    plantilla = models.ForeignKey(Plantilla, on_delete=models.CASCADE)
    detail = models.CharField(max_length = 200)
    date_appointed = models.DateField()
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

contract_status = (
    ('Job Order', 'Job Order',),
    ('Project Based', 'Project Based',),
)

class Contractual(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    positiontitle = models.CharField(max_length = 200)
    status = models.CharField(max_length=50,choices=contract_status)
    basic_salary = models.DecimalField(default= 0,max_digits = 50,decimal_places=2)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date_appointed = models.DateField(default=timezone.now())

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.positiontitle) + ' ' + str(self.profile)
