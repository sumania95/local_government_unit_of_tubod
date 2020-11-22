from django.db import models
from django.db.models import Model, ForeignKey, ManyToManyField
from app_info_profile.models import Profile

class Generate_Ticket(models.Model):
    no_ticket = models.IntegerField(default=0)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.date_created)

class Voucher(models.Model):
    generate_ticket = models.ForeignKey(Generate_Ticket, on_delete=models.CASCADE)
    voucher = models.CharField(max_length = 200)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.voucher)

class Mikrotik(models.Model):
    ip_address = models.GenericIPAddressField()
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    user_profile = models.CharField(max_length = 200)
    user_limit_uptime = models.CharField(max_length = 200)

    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.ip_address)
