# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# Create Custom User Creation Form 
class CustomUserCreationForm(UserCreationForm):
    # Create A Meta Class 
    class Meta(UserCreationForm):
        # Add the Custom User Model and Custom fields to Form 
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age',)

# Create a Custom User Change Form 
class CustomUserChangeForm(UserChangeForm):
    # Create a Meta Class
     class Meta:
         # Add the Custom user Model and Custom fields to Form 
         model = CustomUser
         fields = UserChangeForm.Meta.fields 
