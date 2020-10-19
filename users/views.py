from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login 
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .forms import *
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

def redirect_docs(request):
	return redirect('docs/', permanent=True)


class Login(LoginView):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(Login, self).dispatch(request, *args, **kwargs)
	success_url=reverse_lazy('docs_url')
	template_name=('users/login.html')
	form_class=AuthForm
	

class Logout(LogoutView):
	next_page=reverse_lazy('main_url')

class SignUp(CreateView):
	model = User
	template_name=('users/signup.html')
	form_class=SignUpForm
	success_url=reverse_lazy('docs_url')
	success_msg="Пользователь успешно создан"

	def form_valid(self, form):
		form_valid = super().form_valid(form)
		username = form.cleaned_data['username']
		password = form.cleaned_data['password2']

		auth_user = authenticate(username=username, password=password)
		login(self.request, auth_user)
		return form_valid


