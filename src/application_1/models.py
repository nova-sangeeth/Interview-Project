from django.db import models
from django.contrib.auth.models import User


class UserProfileModel(models.Model):
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=12, choices=gender_choices, blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=256, null=True)
    country = models.CharField(max_length=64, null=True)
    city = models.CharField(max_length=128, null=True)
    pincode = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.user.username


class customer_configuration(models.Model):
    user_id = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE)
    lan_ip = models.GenericIPAddressField()
    organisation_name = models.CharField(null=True, max_length=128)
    plan_start_date = models.DateTimeField()
    plan_end_date = models.DateTimeField()
    current_status = models.BooleanField(default=True)
    created_date = models.DateTimeField()

    def __str__(self):
        return self.organisation_name
