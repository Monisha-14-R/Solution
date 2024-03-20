from django import forms

from Registration.Authentication.models import User


class LoginForm(forms.Form):
    email_or_phone = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['phone_number', 'email', 'password', 'confirm_password']

class ForgetPasswordForm(forms.Form):
    email = forms.EmailField()

class OTPVerificationForm(forms.Form):
    otp = forms.CharField()

class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
