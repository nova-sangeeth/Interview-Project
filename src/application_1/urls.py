from django.conf.urls import url
from .views import register, welcome, login, logout, index, edit_profile, change_password, showthis

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^register/$', register, name="register"),
    url(r'^welcome/$', welcome, name="welcome"),
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^edit_profile/$', edit_profile, name="edit_profile"),
    url(r'^change_password/$', change_password, name="change_password"),
    url(r'^showthis/$', showthis, name="showthis")
]

