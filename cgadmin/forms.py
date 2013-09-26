#coding=utf-8
from django import forms
from django.contrib.auth.models import User


class RegForm(forms.Form):
    username = forms.CharField()
    class Meta:
        model = User
        fields = ('username','password','email')
        widgets = { 'password':forms.PasswordInput()}