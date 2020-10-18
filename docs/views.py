from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.views.generic import View
from .forms import DocumentForm
from .models import DocType, Document

def main(request):
	return render(request, 'docs/main.html')

def news(request):
	return render(request, 'docs/news.html')

def heck(request):
	return render(request, 'docs/heck_i_was_hacked.html')

def add_doc(request):
	return render(request, 'docs/add_doc.html')

def docs(request):
	docs = Document.objects.all()
	types = DocType.objects.all()
	return render(request, 'docs/docs.html', context={'docs': docs, 'types': types})

class DocDetail(View):
	def get(self, request, slug):
		doc = Document.objects.get(slug__iexact=slug)
		types = DocType.objects.all()
		return render(request, 'docs/doc_detail.html', context={'doc': doc, "types": types})
		
class DocCreate(View):
	def get(self, request):
		form = DocumentForm()
		return render(request, 'docs/doc_create.html', context={'form': form})
		
	def post(self, request):
		bounded_form = DocumentForm(request.POST)

		if bounded_form.is_valid():
			new_doc = bounded_form.save()
			return redirect(new_doc)
		return render(request, 'docs/doc_create.html', context={'form': bounded_form})

class DocDelete(View):
	def get(self, request, slug):
		doc = Document.objects.get(slug__iexact=slug)
		return render(request, 'docs/doc_delete.html', context={'doc': doc})
	def post(self, request, slug):
		doc = Document.objects.get(slug__iexact=slug)
		doc.delete()
		return redirect(reverse('main_url'))

def pepe(request):
	return render(request, 'docs/pepe.html')

