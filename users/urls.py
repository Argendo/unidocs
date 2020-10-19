from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', Login.as_view(), name="login_url"),
    path('signup/', SignUp.as_view(), name="signup_url"),
    path('logout/', Logout.as_view(), name="logout_url"),
]
