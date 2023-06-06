from django import forms
from models import Person


class UserForm(forms.ModelForm):
    class Meta:
        model = Person
        widgets = {
        'password': forms.PasswordInput(),
    }