from django.db import models
from django.contrib.auth.models import User


class UserProfileModel(models.Model):
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
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

    # def get_absolute_url(self):
    #     return reverse('user_profile_edit', kwargs={'pk': self.pk})


# class customer_configuration(models.Model):
#     customer_id = models.OneToOneField(
#         UserProfileModel, null=True, on_delete=models.CASCADE)
#     lan_ip = models.GenericIPAddressField()
#     organisation_name = models.CharField(null=True, max_length=128)
#     plan_start_date = models.DateTimeField()
#     plan_end_date = models.DateTimeField()
#     current_status = models.BooleanField(default=True)
#     created_date = models.DateTimeField()

#     def __str__(self):
#         return self.organisation_name


class customer_configuration(models.Model):
    # username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    customer_id = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True)
    lan_IP = models.GenericIPAddressField(null=True)
    organisation_name = models.CharField(max_length=128, null=True)
    white_list_urls = models.URLField(null=True)
    black_list_urls = models.URLField(null=True)
    categories_to_block = models.CharField(max_length=128, null=True)
    countries_to_block = models.CharField(max_length=128, null=True)
    subscription_type = models.CharField(max_length=128, null=True)
    plan_start_date = models.DateTimeField(null=True)
    plan_end_date = models.DateTimeField(null=True)
    current_status = models.BooleanField(null=True)
    created_date = models.DateTimeField(null=True)
    last_modified = models.DateTimeField(null=True)

    def __str__(self):
        return self.organisation_name
