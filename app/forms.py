from django import forms       
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Enter username",
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "Enter password",
    }))
class UserRegistrationForm(UserCreationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text" ,
        "placeholder":"enter username",
        }), label="Username")
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type":"password1",
        "placeholder":"enter your password",
        "id": "password1",  # Add an id for easier selection in JavaScript
        
        })),
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type":"password2",
        "placeholder":"Repeat password",
        "id": "password2",  # Add an id for easier selection in JavaScript
        
        })),
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        

