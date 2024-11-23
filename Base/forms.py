from django import forms

class LoginInput (forms.Form):

  username = forms.CharField (widget=forms.TextInput(attrs={
    'class' : 'form-control',
    'placeholder' : 'Enter user name'
  }))

  password = forms.CharField (widget=forms.TextInput(attrs={
    'class' : 'form-control',
    'type' : 'passowrd'
  }))