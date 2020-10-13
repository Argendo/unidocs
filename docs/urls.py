from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
	path('', main),
	path('news', news),
	path('heck_i_was_hacked', heck),
	path('add_doc', add_doc),
]