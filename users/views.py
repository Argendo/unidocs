from django.shortcuts import render

def login(request):
	return render(request, 'users/login.html')

def logout(request):
	return render(request, 'users/logout.html')

def signup(request):
	return render(request, 'users/signup.html')