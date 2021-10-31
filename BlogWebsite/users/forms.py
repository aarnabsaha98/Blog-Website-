# To add aditional fields int the registartion 
# html file we need to crete this forms.py file to
# enforce the html file to use it.
#https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/

from django import forms
# from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


choose_gender = (

	('1',' '),
	('2', 'male'),
	('3','female'),

)
class userRegisterForm(UserCreationForm):
	email = forms.EmailField()
	gender = forms.ChoiceField(choices = choose_gender)

	# create a class to select the what data
	# from the user registration form 
	# we need to capture 

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2','gender']



class UserUpdateForm(forms.ModelForm):

	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):


	class Meta:
		model = Profile
		fields = ['image']

