from django.db import models
from django.db.models import Model, ForeignKey, ManyToManyField
from model_hris.info_profile.models import Profile

filling = (
    ('Joint', 'Joint',),
    ('Separated', 'Separated',),
    ('Not Applicable', 'Not Applicable',),
)

class Saln_Filling(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    filling_type = models.CharField(max_length=100,blank=True,choices=filling)

##BUSINESS INTEREST AND FINANCIAL CONNECTIONS
class Saln_Business_Interest_Financial_Connections(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    business_enterprise = models.CharField(max_length = 200)
    business_address = models.CharField(max_length = 200,blank=True)
    nature_of_business = models.CharField(max_length = 200,blank=True)
    date_of_acquisition_of_interest = models.DateField()

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

##LIABILITIES
class Saln_Liabilities(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    nature = models.CharField(max_length = 200)
    name_of_creditors = models.CharField(max_length = 200,blank=True)
    outstanding_balance = models.DecimalField(default= 0,max_digits = 50,decimal_places=2)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)



class Saln_Personal_Properties(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.CharField(max_length = 200)
    year = models.IntegerField(default=0)
    acquisition_cost = models.DecimalField(default= 0,max_digits = 50,decimal_places=2)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

class Saln_Real_Properties(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.CharField(max_length = 200)
    kind = models.CharField(max_length = 200,blank=True)
    exact_location = models.CharField(max_length = 200,blank=True)
    assessed_value = models.CharField(max_length = 200,blank=True)
    current_fair_market_value = models.CharField(max_length = 200,blank=True)
    year = models.IntegerField(default=0)
    mode = models.CharField(max_length = 200,blank=True)
    acquisition_cost = models.DecimalField(default= 0,max_digits = 50,decimal_places=2)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)


##RELATIVES IN THE GOVERNMENT SERVICE
class Saln_Relatives_In_The_Government_Service(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name_of_relative = models.CharField(max_length = 200)
    relationship = models.CharField(max_length = 200,blank=True)
    position = models.CharField(max_length = 200,blank=True)
    name_of_agency = models.CharField(max_length = 200,blank=True)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)
