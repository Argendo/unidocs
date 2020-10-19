from django.contrib import admin
from django.urls import include, path
from .views import *


urlpatterns = [
	path('', main, name="main_url"),
	path('news', news, name="news_url"),
	path('heck_i_was_hacked', heck, name="heck_hack_url"),
	path('docs', Docs.as_view(), name="docs_url"),
	path('doc/create/', DocCreate.as_view(), name="doc_create_url"),
	path('doc/<str:slug>/', DocDetail.as_view(), name="doc_detail_url"),
	path('doc/<str:slug>/delete/', DocDelete.as_view(), name="doc_delete_url"),
	path('pepe', pepe, name="eastern_egg_url"),
]