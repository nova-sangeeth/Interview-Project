# Generated by Django 3.0.4 on 2020-04-01 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=12)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('address', models.CharField(max_length=256, null=True)),
                ('country', models.CharField(max_length=64, null=True)),
                ('city', models.CharField(max_length=128, null=True)),
                ('pincode', models.CharField(max_length=10, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='customer_configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lan_ip', models.GenericIPAddressField()),
                ('organisation_name', models.CharField(max_length=128, null=True)),
                ('plan_start_date', models.DateTimeField()),
                ('plan_end_date', models.DateTimeField()),
                ('current_status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField()),
                ('customer_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='application_1.UserProfileModel')),
            ],
        ),
    ]
