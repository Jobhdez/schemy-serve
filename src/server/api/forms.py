from django import forms
from .models import (
    LinearAlgebraCompiler,
    LinearAlgebraInterpreter,
    SchemeInterpreter,
    )
from django.contrib.auth import get_user_model
User = get_user_model()

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class LoginForm(forms.Form):
    """Form that enables the server receive the username and password
    of the given user who is login in"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class LinearAlgebraCompilerForm(forms.Form):
    class Meta:
        model = LinearAlgebraCompiler
        fields = ['input_expression']

class LinearAlgebraInterpreterForm(forms.Form):
    class Meta:
        model = LinearAlgebraInterpreter
        fields = ['input_expression']

class SchemeInterpreterForm(forms.Form):
    class Meta:
        model = SchemeInterpreter
        fields = ['input_expression']

