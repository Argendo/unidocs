from django.shortcuts import render

def main(request):
	return render(request, 'docs/main.html')

def news(request):
	return render(request, 'docs/news.html')

def heck(request):
	return render(request, 'docs/heck_i_was_hacked.html')

def add_doc(request):
	return render(request, 'docs/add_doc.html')