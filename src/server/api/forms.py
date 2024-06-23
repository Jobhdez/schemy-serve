from django import forms
from .models import SchemeInterpreter, Challenges
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

class CompilerForm(forms.Form):
    input_expression = forms.CharField()

class UploadSchemeFile(forms.Form):
    scm_file = forms.FileField()

class ChallengesForm(forms.Form):
  problem_statement = forms.CharField()
  solution = forms.CharField()
