# Generated by Django 3.0.4 on 2020-03-25 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeration',
            name='Phone',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]