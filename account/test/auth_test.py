from unittest import mock

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY
from django.shortcuts import resolve_url
from django.test import TestCase
from django.urls import reverse_lazy


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)

    @mock.patch('two_factor.views.core.signals.user_verified.send')
    def test_login_without_mfa(self, mock_signal):
        # login
        response = self.client.post(reverse_lazy('auth_login'), {
            'auth-username': self.credentials['username'],
            'auth-password': self.credentials['password'],
            'login_view-current_step': 'auth'
        })

        self.assertRedirects(response, resolve_url(settings.LOGIN_REDIRECT_URL))

        # No signal should be sent when user isn't verified against MFA device
        self.assertFalse(mock_signal.called)

    # TODO(devenney): Test login with OTP!
