from django.db import models

class Weather(models.Model):
    date = models.DateField(unique=True)
    was_rainy = models.BooleanField()
