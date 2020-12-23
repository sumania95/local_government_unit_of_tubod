from django.db import models
from model_profiling.tips_person.models import (
    Tips_Person,
)
from model_profiling.tips_address.models import (
    Tips_Barangay,
    Tips_City_Municipality,
    Tips_Province,
    Tips_Region,
)

ownership = (
    ('1','Certificate of Land Transfer'),
    ('2','Emancipation Patent'),
    ('3','Individual Certificate of Land Ownership Award (CLOA)'),
    ('4','Collective CLOA'),
    ('5','Co-ownership CLOA'),
    ('6','Agricultural sales patent'),
    ('7','Homestead patent'),
    ('8','Free Patent'),
    ('9','Certificate of Title or Regular Title'),
    ('10','Certificate of Ancestoral Domain Title'),
    ('11','Certificate of Ancestoral Land Title'),
    ('12','Tax Declaration'),
)

status_ownership = (
    ('1','Registered Owner'),
    ('2','Tenent'),
    ('3','Lessee'),
)

commodity = (
    ('1','Rice'),
    ('2','Corn'),
    ('3','HVC'),
    ('4','Livestock'),
    ('5','Poultry'),
    ('6','Agri-fishery'),
)

farm_type = (
    ('1','Irrigated'),
    ('2','Rainfed Upland'),
    ('3','Rainfed Lowland'),
)


class Tips_Land_Description(models.Model):
    person = models.ForeignKey(Tips_Person, on_delete=models.CASCADE)
    barangay = models.ForeignKey(Tips_Barangay, on_delete=models.CASCADE)
    ownership_document = models.CharField(max_length = 200,choices=ownership)
    size = models.DecimalField(default=0,max_digits = 50,decimal_places=2)
    status = models.CharField(max_length = 200,choices=status_ownership)
    specify = models.CharField(max_length = 200, blank=True)
    commodity = models.CharField(max_length = 200,choices=commodity)
    farm_type = models.CharField(max_length = 200,blank=True,choices=farm_type)
    is_organic = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.commodity)

class Tips_Livestock_Poultry(models.Model):
    land_parcel = models.OneToOneField(Tips_Land_Description, on_delete=models.CASCADE)
    specify = models.CharField(max_length = 200)
    no_of_heads = models.IntegerField(default=0)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.land_parcel)
