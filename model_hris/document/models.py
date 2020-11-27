from django.db import models
from django.db.models import Model, ForeignKey, ManyToManyField

class Document(models.Model):
    name = models.CharField(max_length = 200)
    file = models.FileField(upload_to='forms/')

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
