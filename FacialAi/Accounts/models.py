from django.db import models

from django import forms
from django.contrib.auth.models import User

class Profile(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    mobno1 = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    email = models.EmailField(blank=True)


    def __str__(self):
        return f"{self.full_name} ({self.user.username})"


