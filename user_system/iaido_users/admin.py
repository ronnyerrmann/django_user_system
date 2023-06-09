from django.contrib import admin
from .models import Person

# Without adjusting fields in the admin site
# admin.site.register(Person)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):

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
            'fields': ('username', 'password', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Database automatic process', {
            'fields': ('date_joined', 'last_login')
        }),

    )