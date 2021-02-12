# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser 

# Custom Admin Class to go along with Custom User Class
class CustomUserAdmin(UserAdmin):
    # Add Custom User Creation Form 
    add_form = CustomUserCreationForm
    # Add Custom User Change Form
    form = CustomUserChangeForm 
    # Add Custom user model
    model = CustomUser 
    # Specify what fields to display on Admin Panel
    list_display = ['email', 'username', 'age', 'is_staff', ]

    # Create and Add FieldSets to CustomAdmin Panel 
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', )}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),    
    )
# Register Custom User and Custom Admin on admin set 
admin.site.register(CustomUser, CustomUserAdmin)


# Register your models here.
