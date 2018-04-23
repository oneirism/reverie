from django.contrib.auth import views as auth_views
from django.urls import path, re_path, reverse_lazy
from django.views.generic.base import TemplateView

from registration.backends.default.views import ActivationView, RegistrationView, ResendActivationView
from registration.forms import RegistrationFormUniqueEmail
from two_factor.views import BackupTokensView, DisableView, LoginView, PhoneDeleteView, PhoneSetupView, QRGeneratorView, SetupCompleteView, SetupView

from .views import SettingsView


urlpatterns = [
    path(
        'settings/',
        SettingsView.as_view(),
        name='account_settings'
    ),

    ## USER AUTHENTICATION ##

    path(
        'logout/',
        auth_views.LogoutView.as_view(
            template_name='auth/logout.html'
        ),
        name='auth_logout',
    ),

    ## MFA ##

    path(
        'login/',
        LoginView.as_view(
            template_name='auth/login.html'
        ),
        name='auth_login',
    ),

    path(
        'two_factor/setup/',
        SetupView.as_view(
            template_name='mfa/setup.html',
            success_url='setup_complete',
            qrcode_url='qr'
        ),
        name='setup'
    ),

    path(
        'two_factor/qrcode/',
        QRGeneratorView.as_view(),
        name='qr',
    ),

    path(
        'two_factor/setup/complete/',
        SetupCompleteView.as_view(
            template_name='mfa/setup_complete.html'
        ),
        name='setup_complete',
    ),

    path(
        'two_factor/backup/tokens/',
        BackupTokensView.as_view(
            template_name='mfa/backup_tokens.html',
            success_url='backup_tokens'
        ),
        name='backup_tokens',
    ),

    path(
        'two_factor/backup/phone/register/',
        PhoneSetupView.as_view(
            template_name='mfa/phone_register.html'
        ),
        name='phone_create',
    ),

    path(
        'account/two_factor/backup/phone/unregister/<int:pk>/',
        PhoneDeleteView.as_view(),
        name='phone_delete',
    ),

    path(
        'account/two_factor/disable/',
        view=DisableView.as_view(
            template_name='mfa/disable.html'
        ),
        name='disable',
    ),

    ## USER REGISTRATION ##

    path(
        'register/',
        RegistrationView.as_view(
            form_class=RegistrationFormUniqueEmail,
            template_name='registration/form.html',
        ),
        name='registration_register'
    ),

    path(
        'register/complete',
        TemplateView.as_view(
            template_name='registration/complete.html'
        ),
        name='registration_complete'
    ),

    path(
        'activate/complete',
        TemplateView.as_view(
            template_name='registration/activated.html'
        ),
        name='registration_activation_complete'
    ),

    path(
        'activate/resend',
        ResendActivationView.as_view(
            template_name='registration/resend_activation.html'
        ),
        name='registration_resend_activation'
    ),

    path(
        'activate/<activation_key>',
        ActivationView.as_view(),
        name='registration_activate'
    ),

    ## PASSWORD MANAGEMENT ##

    path(
        'password/change/',
        auth_views.PasswordChangeView.as_view(
            template_name='password_management/password_change.html',
            success_url=reverse_lazy('auth_password_change_done')
        ),
        name='auth_password_change'
    ),

    path(
        'password/change/done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='password_management/password_change_done.html'
        ),
        name='auth_password_change_done'
    ),

    path(
        'password/reset',
        auth_views.PasswordResetView.as_view(
            html_email_template_name='email/password_reset.html',
            template_name='password_management/password_reset.html'
        ),
        name='auth_password_reset'
    ),

    path(
        'password/reset/complete',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='password_management/password_reset_complete.html'
        ),
        name='auth_password_reset_complete'
    ),

    re_path(
        'password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='password_management/password_reset_confirm.html',
            success_url=reverse_lazy('auth_password_reset_complete')
        ),
        name='auth_password_reset_confirm'),

    path(
        'password/reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='password_management/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
]
