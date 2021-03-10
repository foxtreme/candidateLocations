from django.db import models

# Create your models here.
from django.db import models


class University(models.Model):
    name = models.CharField(max_length=60)
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=60)
    province = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    universities = models.ManyToManyField(University, blank=True)

    def __str__(self):
        return self.name


class Economy(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    unemployment_rate = models.DecimalField(max_digits=2, decimal_places=2, verbose_name="Unemployment Rate")
    activities = models.TextField()
