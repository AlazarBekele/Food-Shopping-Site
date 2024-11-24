from django import forms

class LoginInput (forms.Form):

  username = forms.CharField (widget=forms.TextInput(attrs={
    'class' : 'form-control rounded-pill',
    'placeholder' : 'Enter user name'
  }))

  password = forms.CharField (widget=forms.TextInput(attrs={
    'class' : 'form-control rounded-pill',
    'type' : 'passowrd'
  }))