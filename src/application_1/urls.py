from django.conf.urls import url
from .views import register, welcome, login, logout, index

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^register$', register, name="register"),
    url(r'^welcome$', welcome, name="welcome"),
    url(r'^login$', login, name="login"),
    url(r'^logout$', logout, name="logout"),

]
