# from django.contrib.auth.forms import UserCreationForm
from django import forms 

from .models import CustomUser

class RegisterForm(forms.Form):
    
    # username, email, password, first_name 
    user_name = forms.CharField(max_length=200, label='username', 
                                widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    email = forms.CharField(max_length=200, label='email', 
                            widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True)
    first_name = forms.CharField(max_length=200, label='firstname', 
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='password', 
                               widget = forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = CustomUser
        fields = ["user_name", "email", "first_name", "password"]
        
# class LogInForm(forms.Form):
    
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)