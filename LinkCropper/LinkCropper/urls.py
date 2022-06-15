
from datetime import datetime
from django.urls import path, include, reverse
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register/',
        RegistrationView.as_view
        (
            success_url='/', 
            
            form_class=forms.BootstrapRegistrationForm,
            extra_context=
            {
                "title": "Registration"
            }
        ),
        name='register'),

    path('accounts/login/',
        LoginView.as_view
        (

            success_url='home',
            authentication_form=forms.BootstrapAuthenticationForm,
            extra_context=
            {
                'title': 'Log in',
            }
        ),
        name='login'),

    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django_registration.backends.one_step.urls')),

    path('create', views.createNewLink, name='create'),
    path('createname', views.createNewNamedLink, name='createname'),

    path('r/<str:folder>/<int:linkid>', views.reddirectLink, name='reddir'),
    path('r/<str:name>', views.reddirectNameLink, name='reddirName'),
]
