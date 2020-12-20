from django.db import models

class Tips_Region(models.Model):
    region_name = models.CharField(max_length = 255)

    def __str__(self):
        return str(self.region_name)

class Tips_Province(models.Model):
    province_name = models.CharField(max_length = 255)
    region = models.ForeignKey(Tips_Region, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.province_name)

class Tips_City_Municipality(models.Model):
    city_municipality_name = models.CharField(max_length = 255)
    province = models.ForeignKey(Tips_Province, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.city_municipality_name)

class Tips_Barangay(models.Model):
    barangay_name = models.CharField(max_length = 255)
    city_municipality = models.ForeignKey(Tips_City_Municipality, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.barangay_name)
