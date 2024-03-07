from custom_user.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import Account

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields =["email","password1", "password2", "first_name", "last_name"]

class MyModelForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['image','pin','phone','state','postcode','country', 'address','city']