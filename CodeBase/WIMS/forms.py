from django import forms
from .models import Donation, Item
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateItemForm(forms.Form):
    name = forms.CharField(required=True)
    description = forms.CharField(required=True)
    arv = forms.FloatField(required=True)
    weight = forms.FloatField(required=True)
    image = "None"

    class Meta:
        model = Item
        fields = ['name', 'description', 'arv', 'weight', 'image']


class MakeDonationForm(forms.Form):
    quantity = forms.IntegerField(required=True)

    class Meta:
        model = Donation
        fields = ['quantity']
