from django.db import models
from django.db.models import Model, ForeignKey, ManyToManyField
from model_procuremnt.proc_year.models import (
    Proc_Year,
)
from model_procuremnt.proc_classification.models import (
    Proc_Classification,
)

class Proc_Procurement(models.Model):
    name = models.CharField(max_length = 200)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
