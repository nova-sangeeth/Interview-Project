from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm


class usercreate(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=False)
    gender = forms.CharField(required=True)
    city = forms.CharField(required=True)
    phone = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "phone", "gender", "first_name", "last_name",
                  "city", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email

    def clean_password(self):
        return self.initial["password"]

    def save(self, commit=True):
        user = super(usercreate, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.city = self.cleaned_data["city"]
        user.gender = self.cleaned_data["gender"]
        user.phone = self.cleaned_data["phone"]

        if commit:
            user.save()
        return user


class EditUserForm(UserChangeForm):
    template_name = 'change_password.html'

    class Meta:
        model = User
        # fields = '__all__'
        fields = (
            'email',
            'first_name',
            'last_name'
            # 'password'
        )
        exclude = (
            'password',
        )

    def clean_password(self):
        return self.initial["password"]

    # def save(self, commit=True):
    #     user = super(usercreate, self).save(commit=False)
    #     user.email = self.cleaned_data["email"]

    #     if commit:
    #         user.save()
    #     return user
