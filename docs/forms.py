from django import forms
from django.contrib import auth
from django.core.exceptions import ValidationError
from .models import Document, DocType
from django.contrib.auth.models import User

class DocumentForm(forms.Form):
	doc_number = forms.CharField(max_length=100)
	doc_type = forms.ModelChoiceField(queryset=DocType.objects.all())
	slug = forms.CharField(max_length=150, required=False)
	owner = forms.ModelChoiceField(queryset=User.objects.all(), required=False)


	doc_number.widget.attrs.update({'class': 'form-control'})
	slug.widget.attrs.update({'class': 'form-control', 'placeholder': 'Данное поле необязательно'})

	def clean_slug(self):
		new_slug = self.cleaned_data['slug'].lower()

		if new_slug == 'create':
			raise ValidationError('Ссылка не может быть "create"')
		return new_slug

	def save(self):
		new_doc = Document.objects.create(doc_number=self.cleaned_data['doc_number'], doc_type=self.cleaned_data['doc_type'], owner=self.user, slug=self.cleaned_data['slug'])
		return new_doc

	def __init__(self, user, *args, **kwargs):
		self.user = user
		super(DocumentForm, self).__init__(*args, **kwargs)
