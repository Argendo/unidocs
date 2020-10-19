from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm

class AuthForm(AuthenticationForm, forms.ModelForm):
	username = forms.CharField(label=_('Имя пользователя'))
	password = forms.CharField(label=_('Пароль'), widget=forms.PasswordInput)
	
	username.widget.attrs.update({'class': 'form-control'})
	password.widget.attrs.update({'class': 'form-control', "id": "yo"})
	

	class Meta:
			model = User
			fields = (
				'username',
				'password'
				)


class SignUpForm(forms.ModelForm):
	username = forms.CharField(label=_('Имя пользователя'))
	password1 = forms.CharField(label=_('Пароль'), widget=forms.PasswordInput)
	password2 = forms.CharField(label=_('Подтверждение пароля'), widget=forms.PasswordInput)
	
	username.widget.attrs.update({'class': 'form-control'})
	password1.widget.attrs.update({'class': 'form-control', "id": "yo"})
	password2.widget.attrs.update({'class': 'form-control'})

	class Meta:
		model = User
		fields = (
			'username',
			'password1',
			'password2'
			)
	def save(self, commit=True):
		user = super(SignUpForm, self).save(commit=True)
		user.set_password(self.cleaned_data['password2'])
		if commit:
			user.save()

		return user