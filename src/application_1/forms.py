from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import UserProfileModel, customer_configuration


class usercreate(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=False)
    # gender = forms.CharField(required=True)
    # city = forms.CharField(required=True)
    # phone = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ("username", "email",  "first_name",
                  "last_name", "password1", "password2")

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
        # user.city = self.cleaned_data["city"]
        # user.gender = self.cleaned_data["gender"]
        # user.phone = self.cleaned_data["phone"]

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

    def save(self, commit=True):
        if self.is_valid():
            # Get instance with self.instance & only update if a value's changed:
            for field_name in self.fields:
                if getattr(self.instance, field_name) != self.cleaned_data[field_name]:
                    setattr(self.instance, field_name,
                            self.cleaned_data[field_name])
                    self.instance.save()
        return self.instance

    # def clean_password(self):
    #     return self.initial["password"]

    # def save(self, commit=True):
    #     user = super(usercreate, self).save(commit=False)
    #     user.email = self.cleaned_data["email"]

    #     if commit:
    #         user.save()
    #     return user


class userprofile_form(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        # fields = '__all__'
        fields = ('gender', 'age', 'phone_number',
                  'address', 'country', 'city', 'pincode')


class customer_config_form(forms.ModelForm):
    class Meta:
        model = customer_configuration
        fields = ('lan_ip', 'organisation_name', 'plan_start_date',
                  'plan_end_date', 'current_status', 'created_date')
