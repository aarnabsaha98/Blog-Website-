from django.shortcuts import render , redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import userRegisterForm , UserUpdateForm ,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
	if request.method == 'POST':
	# form = UserCreationForm(request.POST)
		# now after having the forms.py file and the enforce 
		#form model to envoke here in place of UserCreationForm
		form = userRegisterForm(request.POST)
		if form.is_valid():
			# unless and untill we do run this save function
			# our user does not get registered to the 
			# server

			form.save()
#form.cleaned_data returns a dictionary of validated form input fields and their values, 
			#where string primary keys are returned as objects.

#form.data returns a dictionary of un-validated form input fields 
			#and their values in string format (i.e. not objects).
			username = form.cleaned_data.get('username')
			messages.success(request, f"{username} Your Profile has been Created")
			return redirect('login')


	else:
		form = userRegisterForm()
	return render(request,'users/register.html',{'form' : form})

@login_required
def profile(request):

	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST,instance=request.user)
		p_form = ProfileUpdateForm(request.POST,
									 
									instance= request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f" Your Account has been Updated")
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance= request.user.profile)
	context = {

		'u_form' : u_form,
		'p_form' : p_form
	}
	return render(request,'users/profile.html',context)