from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout

def signup(request):
	title = 'Signup' 
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('accounts:signin')						
	else:	
		form = UserCreationForm()
	return render(request, 'accounts/signup.html',{'form':form, 'title':title})

def signin(request):
	title = 'Signin'
	if request.method == 'POST':
		form = AuthenticationForm(data = request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request,user)
			return redirect('articles:auther_article')
	else:
		form = AuthenticationForm()
	return render(request, 'accounts/signin.html',{'form':form, 'title':title})

def signout(request):
	logout(request)
	return redirect('articles:all_article')



