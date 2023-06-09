from django import forms
from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import Person
# Without adjusting fields in the admin site
# admin.site.register(Person)


class PasswordForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password", help_text="Leave empty if no change is required", widget=forms.PasswordInput, required=False
    )
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput, required=False
    )
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Person
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'dob', 'is_staff', 'is_active', 'is_superuser',
        'date_joined', 'last_login']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        if not password1 and not self.cleaned_data.get("password"):
            raise ValidationError("Password needs to be given for new user")
        return password2

    def save(self, commit=True):
        # Use the newly given password
        if self.cleaned_data["password1"]:
            user = super().save(commit=False)
            # Hashing will be done in save method of model
            user.password = self.cleaned_data["password1"]
            if commit:
                user.save()
        else:
            user = super().save(commit=commit)
        return user


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    form = PasswordForm
    list_display = (
        'username', 'first_name', 'last_name', 'email', 'phone', 'dob', 'is_staff', 'is_active', 'is_superuser',
        'date_joined', 'last_login'
    )
    readonly_fields = ('date_joined', 'last_login')
    fieldsets = (
        ('Person', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'dob')
        }),
        ('Management', {
            'fields': (
                'username', 'password', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser', 'groups',
                'user_permissions'
            )
        }),
        ('Database automatic process', {
            'fields': ('date_joined', 'last_login')
        }),

    )
