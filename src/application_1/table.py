import django_tables2 as tables
from django.contrib.auth.models import User


class UserTableList(tables.Table):

    class Meta:
        model = User
