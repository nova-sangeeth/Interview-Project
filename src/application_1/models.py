from django.db import models

# Create your models here.


class Registeration(models.Model):
    gender_choices = (
        ('MALE', 'The Gender is Male'),
        ('FEMALE', 'The Gender is female'),
        ('OTHERS', 'The Gender is others'),
        ('NONE', 'The Gender NONE')
    )
    First_name = models.CharField(max_length=256, null=True, blank=False)
    Last_name = models.CharField(max_length=256, null=True, blank=False)
    Gender = models.CharField(
        max_length=128, choices=gender_choices, default='NONE', blank=False)
    Email = models.EmailField(unique=True)
    Phone = models.CharField(
        unique=True, null=True, blank=False, max_length=13)
    City = models.CharField(max_length=128, blank=False)
    Username = models.CharField(
        max_length=128, blank=False, unique=True, null=True)
    Password = models.CharField(max_length=128, blank=False, null=True)

    def __str__(self):
        return self.First_name
