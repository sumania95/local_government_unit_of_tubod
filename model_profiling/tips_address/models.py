from django.db import models

class Tips_Barangay(models.Model):
    barangay_code = models.CharField(max_length = 255)
    barangay_description = models.CharField(max_length = 255)
    region_code =  models.IntegerField()
    province_code = models.IntegerField()
    city_municipality_code = models.IntegerField()

    def __str__(self):
        return str(self.barangay_description)

class Tips_City_Municipality(models.Model):
    psgc_code = models.CharField(max_length = 255)
    city_municipality_code = models.IntegerField()
    city_municipality_description = models.CharField(max_length = 255)
    region_code =  models.IntegerField()
    province_code = models.IntegerField()

    def __str__(self):
        return str(self.city_municipality_description)

class Tips_Province(models.Model):
    psgc_code = models.CharField(max_length = 255)
    province_description = models.CharField(max_length = 255)
    region_code =  models.IntegerField()
    province_code = models.IntegerField()

    def __str__(self):
        return str(self.province_description)

class Tips_Region(models.Model):
    psgc_code = models.CharField(max_length = 255)
    region_description = models.CharField(max_length = 255)
    region_code =  models.IntegerField()

    def __str__(self):
        return str(self.region_description)
