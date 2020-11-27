from django.db import models
from django.db.models import Model, ForeignKey, ManyToManyField

class Proc_Year(models.Model):
    year = models.CharField(max_length = 200)
    is_active = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.year)

    class Meta:
        ordering = ['year']
