from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegisterForm(UserCreationForm):
    username = forms.CharField(help_text='Campo Requerido. Máximo 150 caractéres. Letters, digits and @/./+/-/_ only.')
    email = forms.EmailField() # Omar: Para éste campo por default está como required=True

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2' ]
