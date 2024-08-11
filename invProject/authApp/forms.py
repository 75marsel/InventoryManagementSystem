from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirm Password",
    )
    
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "password_confirm",
        ]
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Password do not match!")
        return cleaned_data
    
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Input your username",
            "class": "form-control",
        })
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Input your password",
            "class": "form-control",
        })
    )