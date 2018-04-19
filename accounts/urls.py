from django.contrib.auth import views as auth_views
from django.urls import include, path, reverse_lazy

from registration.backends.default.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail


urlpatterns = [
    path(
        'register/',
        RegistrationView.as_view(form_class=RegistrationFormUniqueEmail),
        name='registration_register'
    ),

    path(
        'password/reset/',
        auth_views.password_reset,
        {
            'post_reset_redirect': reverse_lazy('auth_password_reset_done'),
            'html_email_template_name': 'registration/password_reset_email.html'
        },
        name='auth_password_reset'
    ),

    path(
        '',
        include('registration.backends.default.urls')
    )
]
