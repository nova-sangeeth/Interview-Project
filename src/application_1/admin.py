from django.contrib import admin
from .models import UserProfileModel, customer_configuration


admin.site.site_header = 'Interview Project Site Administration Login '
admin.site.site_title = 'Interview Project Site Administration Panel'
admin.site.index_title = 'Interview Project Site Dashboard.'

admin.site.register(UserProfileModel)
admin.site.register(customer_configuration)
