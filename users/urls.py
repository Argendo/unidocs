from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
	path('login/', login),
	path('logout/', logout),
	path('signup/', signup),
	
]