from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_view.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm),
         name='login'),
]
