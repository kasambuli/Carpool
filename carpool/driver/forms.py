from django import forms
from .models import Driver
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# profile form
class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['avatar','name','destination']
