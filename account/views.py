from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from two_factor.models import get_available_phone_methods
from two_factor.utils import backup_phones, default_device


@method_decorator(login_required, name='dispatch')
class SettingsView(TemplateView):
    """
    View used by users for managing two-factor configuration.
    This view shows whether two-factor has been configured for the user's
    account. If two-factor is enabled, it also lists the primary verification
    method and backup verification methods.
    """
    template_name = 'profile/settings.html'

    def get_context_data(self, **kwargs):
        try:
            backup_tokens = self.request.user.staticdevice_set.all()[0].token_set.count()
        except Exception:
            backup_tokens = 0

        return {
            'default_device': default_device(self.request.user),
            'default_device_type': default_device(self.request.user).__class__.__name__,
            'backup_phones': backup_phones(self.request.user),
            'backup_tokens': backup_tokens,
            'available_phone_methods': get_available_phone_methods()
        }
