from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
	title = 'Home'
	return render(request, 'welcome.html', {'title':title})
