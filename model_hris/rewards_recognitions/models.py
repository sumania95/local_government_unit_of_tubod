from django.db import models
from django.db.models import Model, ForeignKey, ManyToManyField
from model_hris.info_profile.models import Profile

class Rewards_Recognitions(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    sponsored = models.CharField(max_length = 200)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.title) + ' ' + str(self.profile)
