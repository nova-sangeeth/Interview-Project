from django.conf.urls import url
from .views import register, welcome, login, logout, index,  change_password, showthis, password_reset_confirmation,  customer_config
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^register/$', register, name="register"),
    url(r'^welcome/$', welcome, name="welcome"),
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', logout, name="logout"),

    url(r'^change_password/$', change_password, name="change_password"),
    url(r'^password_reset_confirmation/$', password_reset_confirmation,
        name="password_reset_confirmation"),
    url(r'^showthis/$', showthis, name="showthis"),
    url(r'^customer_config/$', customer_config, name="customer_config"),


    url(r'^password_change/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    url(r'^password_change/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),

    url(r'password_reset/$', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),
        name='password_reset'),
    url(r'^reset/<uidb64>/<token>/$', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_done.html'),
        name='password_reset_confirm'),
    url(r'^password_reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_done'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
]
