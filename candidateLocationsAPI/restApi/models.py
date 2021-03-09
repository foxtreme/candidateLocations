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
    universities = models.ManyToManyField(University)

    def __str__(self):
        return self.name
