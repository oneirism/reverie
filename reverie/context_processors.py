from django.conf import settings
from django.http import HttpRequest

# Google Analytics Context
def google_analytics(request: HttpRequest) -> dict:
    return {
        'GOOGLE_ANALYTICS_KEY': getattr(settings, 'GOOGLE_ANALYTICS_KEY', None),
    }
