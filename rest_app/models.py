from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=100, blank=True)
    abbr_name=models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.abbr_name

class City(models.Model):
    name=models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name

class Zip(models.Model):
    country=models.ForeignKey(Country)
    state=models.ForeignKey(State)
    city=models.ForeignKey(City)
    name=models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name