from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View
from .forms import DocumentForm
from .models import DocType, Document
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.mixins import LoginRequiredMixin

def main(request):
	return render(request, 'docs/main.html')

def news(request):
	return render(request, 'docs/news.html')

def heck(request):
	return render(request, 'docs/heck_i_was_hacked.html')

class Docs(LoginRequiredMixin, View):
	login_url=reverse_lazy('login_url')
	def get(self, request):
		docs = Document.objects.all()
		types = DocType.objects.all()
		return render(request, 'docs/docs.html', context={'docs': docs, 'types': types, 'username': auth.get_user(request).username})

class DocDetail(LoginRequiredMixin, View):
	login_url=reverse_lazy('login_url')
	success_url=reverse_lazy('doc_detail_url')
	def get(self, request, slug):
		doc = Document.objects.get(slug__iexact=slug)
		types = DocType.objects.all()
		raise_exception=True
		return render(request, 'docs/doc_detail.html', context={'doc': doc, "types": types, 'username': auth.get_user(request).username})
		
class DocCreate(LoginRequiredMixin, View):
	login_url=reverse_lazy('login_url')
	redirect_field_name='next'
	def get(self, request):
		form = DocumentForm()
		return render(request, 'docs/doc_create.html', context={'form': form, 'username': auth.get_user(request).username})
		
	def post(self, request):
		bounded_form = DocumentForm(request.POST)

		if bounded_form.is_valid():
			new_doc = bounded_form.save()
			return redirect(new_doc)
		return render(request, 'docs/doc_create.html', context={'form': bounded_form, 'username': auth.get_user(request).username})

class DocDelete(LoginRequiredMixin, View):
	login_url=reverse_lazy('login_url')
	success_url=reverse_lazy('doc_detail_url')
	def get(self, request, slug):
		doc = Document.objects.get(slug__iexact=slug)
		return render(request, 'docs/doc_delete.html', context={'doc': doc, 'username': auth.get_user(request).username})
	def post(self, request, slug):
		doc = Document.objects.get(slug__iexact=slug)
		doc.delete()
		return redirect(reverse_lazy('main_url'))

def pepe(request):
	return render(request, 'docs/pepe.html')

