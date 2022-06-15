from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django_registration.forms import RegistrationForm


class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control w-100',
                                   'placeholder': 'Username',
                                   'aria-label': 'Username',
                                   'aria-describedby': 'basic-addon1'
                                   }))

    password = forms.CharField(widget=forms.PasswordInput({
                                   'class': 'form-control w-100',
                                   'placeholder':'Password',
                                   'aria-label': 'Password',
                                   'aria-describedby': 'basic-addon1'
                                   }))

class BootstrapRegistrationForm(RegistrationForm):
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Username',
                                   'aria-label': 'Username',
                                   'aria-describedby': 'basic-addon1'
                                   }))
    email = forms.EmailField(max_length=254,
                               widget=forms.EmailInput({
                                   'class': 'form-control',
                                   'placeholder': 'Email',
                                   'aria-label': 'Email',
                                   'aria-describedby': 'basic-addon1'
                                   }))

    password1 = forms.CharField(widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password',
                                   'aria-label': 'Password',
                                   'aria-describedby': 'basic-addon1'
                                   }))

    password2 = forms.CharField(widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password',
                                   'aria-label': 'Password',
                                   'aria-describedby': 'basic-addon1'
                                   }))


class BootstrapCreateLinkForm(AuthenticationForm):
    url = forms.URLField(widget=forms.URLInput({
                                   'class': 'form-control form-control-lg container-md',
                          }))

class BootstrapCreateNameLinkForm(AuthenticationForm):
    url = forms.URLField(widget=forms.URLInput({
                                   'class': 'form-control form-control-lg container-md',
                          }))
    name = forms.CharField(widget=forms.TextInput({
                                   'class': 'form-control form-control-lg container-md',
                                   'placeholder':'Name',
                                   'aria-label': 'Name',
                                   'aria-describedby': 'basic-addon1'
                          }))