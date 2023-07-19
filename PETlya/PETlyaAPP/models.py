from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    pet_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    problem = models.TextField(blank=True)

