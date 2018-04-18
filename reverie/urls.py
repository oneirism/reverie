"""reverie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path, reverse_lazy

from registration.backends.default.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/register/', RegistrationView.as_view(form_class=RegistrationFormUniqueEmail),
        name='registration_register'),
    path('accounts/password/reset/',
        auth_views.password_reset, {
            'post_reset_redirect': reverse_lazy('auth_password_reset_done'),
            'html_email_template_name': 'registration/password_reset_email.html'
        }, name='auth_password_reset'),
    path('accounts/', include('registration.backends.default.urls')),
]
