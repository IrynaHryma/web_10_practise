from django.contrib import admin
from django.urls import path

from .forms import LoginForm
from . import views
from django.contrib.auth.views import LoginView, LogoutView

from .views import RegisterView

app_name = "users"



urlpatterns = [
    path('signup/', RegisterView.as_view(),name="register"),
    path('signin/', LoginView.as_view(template_name="users/signin.html",    authentication_form =LoginForm, redirect_authenticated_user=True),name="login"),
    # path('logout/', LogoutView.as_view(),name="logout"),
    

]
