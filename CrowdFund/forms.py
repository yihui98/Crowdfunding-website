from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import NewProject


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = NewProject
        fields = [
            'donor',
            'name',
            'description',
            'price',
            ]
        labels = {
            'name' : 'Project Name',
            'price' : 'Funding amount'
            }
        widgets = {'donor' : forms.HiddenInput()}

class DonationForm(forms.ModelForm):
    class Meta:
        model = NewProject
        fields = [
            'fund_raised'
            ]
        labels = {
            'fund_raised' : 'Donation Amount'
            }

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

        
