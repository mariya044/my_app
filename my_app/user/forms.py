from django import forms
from user.models import MyUser


class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ("username","password","email","groups","first_name","last_name","phone")