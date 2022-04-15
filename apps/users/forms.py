from .models import User
from django import forms
from django.contrib.auth import authenticate

class UserRegisterForm(forms.ModelForm):
    """Form definition for UserRegister."""
    password2 = forms.CharField(
        max_length=100,required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'minlength':'6'
            }
        )
    )
    class Meta:
        """Meta definition for usernameform."""
        model = User
        fields = ('username','password')
        widgets ={
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                }
            ),
            'password': forms.TextInput(attrs={
                'class': 'form-control',
                'type':'password',
                'minlength':'6',
            }),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = User.objects.filter(username=username)
        if user:
            self.add_error('username','El usuario ya existe')
        return username

    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')
        password = self.cleaned_data.get('password')
        if not password2 == password:
            self.add_error('password2','Las contraseñas no coinciden') 
        return password2

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
        attrs={
        'type': 'text',
        'class': 'form-control',
        'placeholder':'usuario'
    }))
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
        attrs={
        'class': 'form-control',
        'placeholder':'Contraseña'
    }))

    #Validate that the two password are the same
    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if not authenticate(username=username, password=password):
            self.add_error('username','El usuario no existe')
        return password