from django import forms
from .models import Donation, Item
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',  'password1', 'password2']


class CreateItemForm(forms.Form):
    name = forms.CharField(required=True)
    description = forms.CharField(required=True)
    arv = forms.FloatField(required=True)

    class Meta:
        model = Item
        fields = ['name', 'description', 'arv', 'weight', 'image']


class MakeDonationForm(forms.Form):
    quantity = forms.IntegerField(required=True)

    class Meta:
        model = Donation
        fields = ['quantity']
